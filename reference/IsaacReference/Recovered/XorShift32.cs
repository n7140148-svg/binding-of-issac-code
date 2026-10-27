namespace IsaacReference.Recovered;

public readonly record struct ShiftTriple(int Right1, int Left, int Right2)
{
    public static ShiftTriple Collectible => new(3, 5, 20);
    public static ShiftTriple Retry => new(1, 11, 6);
    public static ShiftTriple Challenge => new(1, 5, 19);
    public static ShiftTriple Wave => new(5, 9, 7);
    public static ShiftTriple StartSeed => new(3, 23, 25);
}

public readonly record struct XorShiftSnapshot(uint State, ShiftTriple Shifts);

// Evidence: 007a7d50, 007a7db0, 005b6370; constants: evidence/pe-constants.json.
public sealed class XorShift32
{
    public uint State { get; private set; }
    public ShiftTriple Shifts { get; }

    public XorShift32(uint seed, ShiftTriple shifts)
    {
        // The binary logs and traps on zero; the managed API throws instead.
        if (seed == 0) throw new ArgumentOutOfRangeException(nameof(seed));
        State = seed;
        Shifts = shifts;
    }

    public uint NextUInt()
    {
        var x = State;
        if (x == 0) throw new InvalidOperationException("The RNG reached a zero state.");
        x ^= x >> (Shifts.Right1 & 31);
        x ^= x << (Shifts.Left & 31);
        x ^= x >> (Shifts.Right2 & 31);
        State = x;
        return x;
    }

    public uint NextInt(uint bound)
    {
        var x = NextUInt();
        return bound == 0 ? 0 : x % bound;
    }

    public float NextFloat()
    {
        float unsignedAsSingle = NextUInt();
        return unsignedAsSingle * BitConverter.UInt32BitsToSingle(0x2f7ffffe);
    }

    public void Shuffle<T>(Span<T> entries)
    {
        for (var i = entries.Length - 1; i > 0; i--)
        {
            var j = (int)NextInt((uint)i + 1);
            (entries[i], entries[j]) = (entries[j], entries[i]);
        }
    }

    public XorShiftSnapshot Capture() => new(State, Shifts);
    public static XorShift32 Restore(XorShiftSnapshot snapshot) => new(snapshot.State, snapshot.Shifts);
}
