using IsaacReference.Recovered;

namespace IsaacReference.Original;

public readonly record struct PlayerDamageRequest(float Amount, ulong Flags, int SourceId, int Cooldown);
public readonly record struct PlayerDamageResult(bool Accepted, float QueuedAmount, ulong QueuedFlags);

// Independent model of the Lua TakeDamage wrapper at 00819e70/00846fb0.
// Native player dispatch receives the amount, flags, source and cooldown and
// returns a boolean. HP/death consumption remains a separate host policy.
public sealed class PlayerCombat
{
    public PendingDamage Pending { get; }

    public PlayerCombat(PendingDamage? pending = null) => Pending = pending ?? new();

    public PlayerDamageResult TakeDamage(PlayerDamageRequest request,
        Func<PlayerDamageRequest, bool>? nativeDispatch = null)
    {
        if (!float.IsFinite(request.Amount) || request.Cooldown < 0)
            throw new ArgumentOutOfRangeException(nameof(request));
        if (nativeDispatch is not null && !nativeDispatch(request))
            return new(false, Pending.Amount, Pending.Flags);
        var accepted = Pending.TryQueue(new(request.Amount, request.Flags, request.SourceId, request.Cooldown));
        return new(accepted, Pending.Amount, Pending.Flags);
    }
}
