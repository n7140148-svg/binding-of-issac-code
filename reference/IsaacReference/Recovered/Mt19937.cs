namespace IsaacReference.Recovered;

public sealed record MtSnapshot(uint[] Words, int Index);

// Evidence: 006c3d50 and 006c3d90. State persistence is a reference API.
public sealed class Mt19937
{
    private readonly uint[] words = new uint[624];
    private int index = 624;

    public Mt19937(uint seed = 5489)
    {
        words[0] = seed;
        for (uint i = 1; i < words.Length; i++)
            words[i] = unchecked(1812433253U * (words[i - 1] ^ (words[i - 1] >> 30)) + i);
    }

    public uint NextUInt()
    {
        if (index == words.Length)
        {
            for (var i = 0; i < words.Length; i++)
            {
                var joined = (words[i] & 0x80000000U) | (words[(i + 1) % 624] & 0x7fffffffU);
                words[i] = words[(i + 397) % 624] ^ (joined >> 1) ^
                    ((joined & 1) != 0 ? 0x9908b0dfU : 0);
            }
            index = 0;
        }
        var y = words[index++];
        y ^= y >> 11;
        y ^= (y << 7) & 0x9d2c5680U;
        y ^= (y << 15) & 0xefc60000U;
        return y ^ (y >> 18);
    }

    public MtSnapshot Capture() => new((uint[])words.Clone(), index);

    public static Mt19937 Restore(MtSnapshot snapshot)
    {
        ArgumentNullException.ThrowIfNull(snapshot);
        if (snapshot.Words is not { Length: 624 } || snapshot.Index is < 0 or > 624 ||
            !snapshot.Words.Any(w => w != 0))
            throw new ArgumentException("Invalid MT19937 state.", nameof(snapshot));
        var result = new Mt19937();
        snapshot.Words.CopyTo(result.words, 0);
        result.index = snapshot.Index;
        return result;
    }
}
