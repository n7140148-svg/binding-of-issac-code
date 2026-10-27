namespace IsaacReference.Recovered;

public readonly record struct SpawnEntry(int Type, ushort Variant, ushort Subtype, float Weight);

// Evidence: 007e7c20. For valid nonempty configurations, failure selects entry zero.
public static class WeightedSpawn
{
    public static SpawnEntry Pick(IReadOnlyList<SpawnEntry> entries, float sample)
    {
        if (entries.Count is < 1 or > 255) throw new ArgumentOutOfRangeException(nameof(entries));
        if (!float.IsFinite(sample) || sample < 0 || sample > 1)
            throw new ArgumentOutOfRangeException(nameof(sample));
        float total = 0;
        foreach (var entry in entries)
        {
            if (!float.IsFinite(entry.Weight) || entry.Weight < 0)
                throw new ArgumentException("Weights must be finite and nonnegative.", nameof(entries));
            total += entry.Weight;
        }
        if (!float.IsFinite(total)) throw new ArgumentException("Weight sum overflow.", nameof(entries));
        float cumulative = 0;
        foreach (var entry in entries)
        {
            cumulative += entry.Weight;
            if (sample * total < cumulative) return entry;
        }
        return entries[0];
    }
}
