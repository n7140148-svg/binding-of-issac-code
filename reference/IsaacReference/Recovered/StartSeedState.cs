namespace IsaacReference.Recovered;

public sealed record StartSeedSnapshot(uint StartSeed, uint[] StageSeeds, uint AdditionalSeed, XorShiftSnapshot Stream);

// Evidence: 0093e220 initializes 14 stage slots and one additional value;
// 00705f30 reads a stage slot; 006c4560 advances the stream and leaves it in EAX.
public sealed class StartSeedState
{
    private readonly uint[] stageSeeds = new uint[14];
    private readonly XorShift32 stream;
    public uint StartSeed { get; }
    public uint AdditionalSeed { get; }

    public StartSeedState(uint seed, Mt19937? globalGenerator = null)
    {
        if (seed == 0)
        {
            if (globalGenerator is null)
                throw new ArgumentException("Seed zero requires the host's global MT19937 instance.", nameof(globalGenerator));
            seed = Math.Max(1U, globalGenerator.NextUInt());
        }
        StartSeed = seed;
        stream = new(seed, ShiftTriple.StartSeed);
        for (var i = 0; i < stageSeeds.Length; i++) stageSeeds[i] = stream.NextUInt();
        AdditionalSeed = stream.NextUInt();
    }

    private StartSeedState(StartSeedSnapshot snapshot)
    {
        if (snapshot.StartSeed == 0 || snapshot.AdditionalSeed == 0 || snapshot.StageSeeds is not { Length: 14 } ||
            snapshot.StageSeeds.Any(s => s == 0) || snapshot.Stream.Shifts != ShiftTriple.StartSeed)
            throw new ArgumentException("Invalid start seed state.", nameof(snapshot));
        StartSeed = snapshot.StartSeed;
        AdditionalSeed = snapshot.AdditionalSeed;
        snapshot.StageSeeds.CopyTo(stageSeeds, 0);
        stream = XorShift32.Restore(snapshot.Stream);
    }

    public uint GetStageSeed(int stageIndex)
    {
        if ((uint)stageIndex >= stageSeeds.Length) throw new ArgumentOutOfRangeException(nameof(stageIndex));
        return stageSeeds[stageIndex];
    }

    public uint NextSeed() => stream.NextUInt();
    public StartSeedSnapshot Capture() => new(StartSeed, (uint[])stageSeeds.Clone(), AdditionalSeed, stream.Capture());
    public static StartSeedState Restore(StartSeedSnapshot snapshot) => new(snapshot);
}
