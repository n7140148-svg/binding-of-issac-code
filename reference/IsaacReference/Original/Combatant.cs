using IsaacReference.Recovered;

namespace IsaacReference.Original;

// Original HP application policy, deliberately separate from recovered queuing.
public sealed class Combatant
{
    public float HitPoints { get; private set; }
    public bool Dead => HitPoints <= 0;
    public PendingDamage Pending { get; }

    public Combatant(float hitPoints, PendingDamage? pending = null)
    {
        if (!float.IsFinite(hitPoints) || hitPoints < 0) throw new ArgumentOutOfRangeException(nameof(hitPoints));
        HitPoints = hitPoints;
        Pending = pending ?? new();
    }

    public bool Hit(DamageRequest request) => Pending.TryQueue(request, r => !Dead && r.Amount > 0);

    public float ApplyPending()
    {
        var before = HitPoints;
        foreach (var request in Pending.Drain()) HitPoints = Math.Max(0, HitPoints - Math.Max(0, request.Amount));
        return before - HitPoints;
    }
}
