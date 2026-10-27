using System.Globalization;
using System.Xml;
using System.Xml.Linq;

namespace IsaacReference.Recovered;

[Flags]
public enum PoolFlags : uint
{
    None = 0,
    PreserveWeight = 1,
    ExcludeType3AndExtendRepicks = 2,
    RequireType3 = 8
}

public sealed record PoolEntry(int Id, float BaseWeight, float RemainingWeight,
    float DecreaseBy, float RemoveOn, int ItemType = 0);

public sealed record PoolSnapshot(PoolEntry[] Entries, int[] Excluded);

// The 00700c60 weighted/depletion core. The GetCollectible wrapper's special
// cases, callbacks, unlocks and global exclusion policies are not reproduced.
public sealed class ItemPool
{
    private readonly List<PoolEntry> entries;
    private readonly HashSet<int> excluded;
    public IReadOnlyList<PoolEntry> Entries => entries.AsReadOnly();
    public IReadOnlySet<int> Excluded => new HashSet<int>(excluded);
    public float TotalBaseWeight { get; }

    public ItemPool(IEnumerable<PoolEntry> entries, IEnumerable<int>? excluded = null)
    {
        this.entries = entries.ToList();
        foreach (var entry in this.entries)
            if (!float.IsFinite(entry.BaseWeight) || entry.BaseWeight < 0 ||
                !float.IsFinite(entry.RemainingWeight) || entry.RemainingWeight < 0 ||
                !float.IsFinite(entry.DecreaseBy) || entry.DecreaseBy < 0 ||
                !float.IsFinite(entry.RemoveOn) || entry.RemoveOn < 0)
                throw new ArgumentException("Invalid pool weights.", nameof(entries));
        float total = 0;
        foreach (var entry in this.entries) total += entry.BaseWeight;
        if (!float.IsFinite(total)) throw new ArgumentException("Weight sum overflow.", nameof(entries));
        TotalBaseWeight = total;
        this.excluded = excluded is null ? [] : new HashSet<int>(excluded);
    }

    public PoolEntry? Draw(XorShift32 rng, PoolFlags flags = PoolFlags.None,
        Func<PoolEntry, bool>? eligible = null, bool excludeOnRemoval = true)
        => Select(rng.NextFloat(), flags, eligible, excludeOnRemoval);

    public PoolEntry? Select(float sample, PoolFlags flags = PoolFlags.None,
        Func<PoolEntry, bool>? eligible = null, bool excludeOnRemoval = true)
    {
        if (!float.IsFinite(sample) || sample < 0 || sample >= 1)
            throw new ArgumentOutOfRangeException(nameof(sample));
        if (entries.Count == 0 || TotalBaseWeight <= 0) return null;
        var scaled = sample * TotalBaseWeight;
        var budget = flags.HasFlag(PoolFlags.ExcludeType3AndExtendRepicks) ? 20 : 10;
        while (true)
        {
            float cumulative = 0;
            var selected = -1;
            for (var i = 0; i < entries.Count; i++)
            {
                cumulative += entries[i].BaseWeight;
                if (cumulative > scaled) { selected = i; break; }
            }
            if (selected < 0) return null;
            var entry = entries[selected];
            var residualFromRight = (cumulative - scaled) / entry.BaseWeight;
            var acceptance = 1f - residualFromRight;
            if (acceptance < entry.RemainingWeight / entry.BaseWeight && Allowed(entry))
                return Consume(selected);

            if (budget-- == 0)
            {
                // Native exhaustion fallback excludes the final rejected entry.
                for (var step = 1; step < entries.Count; step++)
                {
                    var next = (selected + step) % entries.Count;
                    if (entries[next].RemainingWeight > 0 && Allowed(entries[next])) return Consume(next);
                }
                return null;
            }
            scaled = TotalBaseWeight * residualFromRight;
            if (scaled == TotalBaseWeight)
                scaled = TotalBaseWeight / BitConverter.UInt32BitsToSingle(0x4057e204);
        }

        bool Allowed(PoolEntry entry) => !excluded.Contains(entry.Id) &&
            (!flags.HasFlag(PoolFlags.ExcludeType3AndExtendRepicks) || entry.ItemType != 3) &&
            (!flags.HasFlag(PoolFlags.RequireType3) || entry.ItemType == 3) &&
            (eligible?.Invoke(entry) ?? true);

        PoolEntry Consume(int i)
        {
            var entry = entries[i];
            if (entry.RemainingWeight > 0 && !flags.HasFlag(PoolFlags.PreserveWeight))
            {
                var remaining = entry.RemainingWeight - entry.DecreaseBy;
                if (remaining < entry.RemoveOn)
                {
                    remaining = 0;
                    // Game-specific challenge and side-effect rules are policy hooks.
                    if (excludeOnRemoval && entry.Id >= 0) excluded.Add(entry.Id);
                }
                entries[i] = entry with { RemainingWeight = remaining };
            }
            return entries[i];
        }
    }

    public PoolSnapshot Capture() => new(entries.ToArray(), excluded.Order().ToArray());
    public static ItemPool Restore(PoolSnapshot snapshot) => new(snapshot.Entries, snapshot.Excluded);

    // A strict standalone loader for ordinary entries. Mod merge policy is omitted.
    public static IReadOnlyDictionary<string, ItemPool> LoadXml(Stream input)
    {
        using var reader = XmlReader.Create(input, new XmlReaderSettings { DtdProcessing = DtdProcessing.Prohibit });
        var document = XDocument.Load(reader);
        if (document.Root?.Name.LocalName != "ItemPools") throw new FormatException("Expected ItemPools root.");
        var pools = new Dictionary<string, ItemPool>(StringComparer.Ordinal);
        foreach (var pool in document.Root.Elements("Pool"))
        {
            var name = (string?)pool.Attribute("Name") ?? throw new FormatException("Missing pool Name.");
            var list = new List<PoolEntry>();
            foreach (var item in pool.Elements("Item"))
            {
                var id = int.Parse(Required(item, "Id"), CultureInfo.InvariantCulture);
                var weight = Number(item, "Weight");
                list.Add(new(id, weight, weight, Number(item, "DecreaseBy"), Number(item, "RemoveOn")));
            }
            if (!pools.TryAdd(name, new ItemPool(list))) throw new FormatException("Duplicate pool: " + name);
        }
        return pools;

        static string Required(XElement e, string name) => (string?)e.Attribute(name) ??
            throw new FormatException("Missing " + name + ".");
        static float Number(XElement e, string name) => float.Parse(Required(e, name), CultureInfo.InvariantCulture);
    }
}
