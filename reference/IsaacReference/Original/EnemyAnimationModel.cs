namespace IsaacReference.Original;

public enum EnemyPhase { Uninitialized = 0, Idle = 4, Leap = 6, DirectionalAttack = 8, Summon = 13, Scream = 16 }
public enum AttackDirection { Left, Up, Right, Down }
public enum EnemyCommand { Projectile, SummonMinion, LandingEffect, ScreamFinished }
public sealed record EnemyInput(bool Scream = false, bool Shoot = false, bool Summon = false,
    bool Leap = false, bool AnimationFinished = false, bool ShootEvent = false,
    bool LandingEvent = false, int ExistingMinions = 0, float TargetX = 0, float TargetY = 0);
public sealed record EnemySnapshot(EnemyPhase Phase, int Frames, AttackDirection Direction);

// A host-driven model of selected branches at 0044e9a0. Eligibility decisions,
// animation playback and physics remain external; no enemy identity is asserted.
public sealed class EnemyAnimationModel
{
    public EnemyPhase Phase { get; private set; }
    public int Frames { get; private set; }
    public AttackDirection Direction { get; private set; }

    public EnemyCommand[] Tick(EnemyInput input, int elapsed = 1)
    {
        if (elapsed < 0 || input.ExistingMinions < 0 || !float.IsFinite(input.TargetX) || !float.IsFinite(input.TargetY))
            throw new ArgumentOutOfRangeException(nameof(input));
        var commands = new List<EnemyCommand>();
        if (Phase == EnemyPhase.Uninitialized) { Enter(EnemyPhase.Idle); return []; }
        Frames = checked(Frames + elapsed);
        switch (Phase)
        {
            case EnemyPhase.Idle:
                if (input.Scream) Enter(EnemyPhase.Scream);
                else if (input.Shoot)
                {
                    Direction = MathF.Abs(input.TargetY) <= MathF.Abs(input.TargetX)
                        ? (input.TargetX < 0 ? AttackDirection.Left : AttackDirection.Right)
                        : (input.TargetY >= 0 ? AttackDirection.Down : AttackDirection.Up);
                    Enter(EnemyPhase.DirectionalAttack);
                }
                else if (input.Summon && input.ExistingMinions < 3) Enter(EnemyPhase.Summon);
                else if (input.Leap) Enter(EnemyPhase.Leap);
                break;
            case EnemyPhase.DirectionalAttack:
                if (input.ShootEvent) commands.Add(EnemyCommand.Projectile);
                if (input.AnimationFinished) Enter(EnemyPhase.Idle);
                break;
            case EnemyPhase.Summon:
                if (input.ShootEvent)
                    for (var i = input.ExistingMinions; i < 4; i++) commands.Add(EnemyCommand.SummonMinion);
                if (input.AnimationFinished) Enter(EnemyPhase.Idle);
                break;
            case EnemyPhase.Leap:
                if (input.LandingEvent) commands.Add(EnemyCommand.LandingEffect);
                if (input.AnimationFinished) Enter(EnemyPhase.Idle);
                break;
            case EnemyPhase.Scream:
                if (input.AnimationFinished) { commands.Add(EnemyCommand.ScreamFinished); Enter(EnemyPhase.Idle); }
                break;
        }
        return commands.ToArray();
    }

    private void Enter(EnemyPhase phase) { Phase = phase; Frames = 0; }
    public EnemySnapshot Capture() => new(Phase, Frames, Direction);
    public static EnemyAnimationModel Restore(EnemySnapshot snapshot)
    {
        if (!Enum.IsDefined(snapshot.Phase) || !Enum.IsDefined(snapshot.Direction) || snapshot.Frames < 0)
            throw new ArgumentException("Invalid enemy state.", nameof(snapshot));
        return new() { Phase = snapshot.Phase, Frames = snapshot.Frames, Direction = snapshot.Direction };
    }
}
