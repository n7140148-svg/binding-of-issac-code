namespace IsaacReference.Recovered;

public readonly record struct DamageRequest(float Amount, ulong Flags, int SourceId, int Cooldown);
public sealed record DamageSnapshot(int Gate2, int Gate40, DamageRequest[] Events);

// Selected ordinary-path behavior of 00684bb0 plus the event append at 0068f0f0.
// Caller supplies eligibility/scaling; this class never interprets pending damage as HP.
public sealed class PendingDamage
{
    private readonly List<DamageRequest> events = [];
    public int Gate2 { get; private set; }
    public int Gate40 { get; private set; }
    public IReadOnlyList<DamageRequest> Events => events.AsReadOnly();
    public float Amount { get; private set; }
    public ulong Flags { get; private set; }

    public bool TryQueue(DamageRequest request, Func<DamageRequest, bool>? accept = null)
    {
        if (!float.IsFinite(request.Amount) || request.Cooldown < 0)
            throw new ArgumentOutOfRangeException(nameof(request));
        if ((request.Flags & 2) != 0 && request.Amount > 0)
        {
            if (Gate2 > 0) return false;
            Gate2 = 10;
        }
        if ((request.Flags & 0x40) != 0)
        {
            if (Gate40 > 0) return false;
            Gate40 = request.Cooldown;
        }
        // The native cooldown writes precede callback rejection. Do not roll them back.
        if (!(accept?.Invoke(request) ?? true)) return false;
        events.Add(request);
        Amount += request.Amount;
        Flags |= request.Flags;
        return true;
    }

    // Explicit host timing policy: cooldown decrement sites have not been traced.
    public void AdvanceHostTicks(int ticks = 1)
    {
        if (ticks < 0) throw new ArgumentOutOfRangeException(nameof(ticks));
        Gate2 = Math.Max(0, Gate2 - ticks);
        Gate40 = Math.Max(0, Gate40 - ticks);
    }

    public DamageRequest[] Drain()
    {
        var result = events.ToArray();
        events.Clear();
        Amount = 0;
        Flags = 0;
        return result;
    }

    public DamageSnapshot Capture() => new(Gate2, Gate40, events.ToArray());

    public static PendingDamage Restore(DamageSnapshot snapshot)
    {
        if (snapshot.Gate2 < 0 || snapshot.Gate40 < 0 || snapshot.Events is null ||
            snapshot.Events.Any(e => !float.IsFinite(e.Amount) || e.Cooldown < 0))
            throw new ArgumentException("Invalid damage state.", nameof(snapshot));
        var result = new PendingDamage { Gate2 = snapshot.Gate2, Gate40 = snapshot.Gate40 };
        foreach (var entry in snapshot.Events)
        {
            result.events.Add(entry);
            result.Amount += entry.Amount;
            result.Flags |= entry.Flags;
        }
        return result;
    }
}
