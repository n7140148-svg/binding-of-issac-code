using System.Text;
using System.Text.Json;
using IsaacReference.Original;
using IsaacReference.Recovered;

namespace IsaacReference.Runner;

internal static class Verification
{
    private sealed record XorVector(uint Seed, int[] Shifts, uint[] Values, uint[] FloatBits);
    private sealed record SeedVector(uint Seed, string Text);
    private sealed record Vectors(XorVector[] Xorshift, SeedVector[] Seeds, uint[] MtDefaultFirstTen);
    private static int passed;
    private static int failed;

    public static int Run()
    {
        passed = failed = 0;
        var vectors = JsonSerializer.Deserialize<Vectors>(File.ReadAllText(Path.Combine(AppContext.BaseDirectory, "reference-vectors.json")), Program.Json)!;
        foreach (var vector in vectors.Xorshift)
        {
            Check($"xorshift/float bits seed={vector.Seed} shifts={string.Join(',', vector.Shifts)}", () =>
            {
                var shifts = new ShiftTriple(vector.Shifts[0], vector.Shifts[1], vector.Shifts[2]);
                var integer = new XorShift32(vector.Seed, shifts);
                var single = new XorShift32(vector.Seed, shifts);
                for (var i = 0; i < vector.Values.Length; i++)
                {
                    Equal(vector.Values[i], integer.NextUInt());
                    Equal(vector.FloatBits[i], BitConverter.SingleToUInt32Bits(single.NextFloat()));
                }
            });
        }
        Check("zero seed rejected", () => Throws<ArgumentOutOfRangeException>(() => new XorShift32(0, ShiftTriple.Wave)));
        Check("zero bound consumes one draw", () =>
        {
            var a = new XorShift32(1, ShiftTriple.Collectible);
            var b = new XorShift32(1, ShiftTriple.Collectible);
            Equal(0U, a.NextInt(0)); b.NextUInt(); Equal(b.State, a.State);
        });
        Check("shuffle preserves entries and consumes n-1 draws", () =>
        {
            var rng = new XorShift32(42, ShiftTriple.Wave);
            var control = XorShift32.Restore(rng.Capture());
            var entries = Enumerable.Range(0, 20).ToArray();
            rng.Shuffle(entries.AsSpan());
            for (var i = 1; i < entries.Length; i++) control.NextUInt();
            Equal(control.State, rng.State);
            Sequence(Enumerable.Range(0, 20), entries.Order());
            rng.Shuffle(Span<int>.Empty); Equal(control.State, rng.State);
            rng.Shuffle(new int[1].AsSpan()); Equal(control.State, rng.State);
        });
        Check("MT19937 default known sequence", () =>
        {
            var mt = new Mt19937();
            Sequence(vectors.MtDefaultFirstTen, Enumerable.Range(0, 10).Select(_ => mt.NextUInt()));
        });
        Check("MT state replay across twist boundaries", () =>
        {
            var mt = new Mt19937(123);
            for (var i = 0; i < 623; i++) mt.NextUInt();
            var saved = RoundTrip(mt.Capture());
            var restored = Mt19937.Restore(saved);
            for (var i = 0; i < 2000; i++) Equal(mt.NextUInt(), restored.NextUInt());
            saved.Words[0] ^= 123;
            Equal(mt.NextUInt(), restored.NextUInt());
        });
        foreach (var vector in vectors.Seeds)
            Check($"seed codec fixed vector {vector.Seed}", () =>
            {
                Equal(vector.Text, SeedCodec.Encode(vector.Seed));
                True(SeedCodec.TryDecode(vector.Text, out var decoded)); Equal(vector.Seed, decoded);
            });
        Check("seed checksum and strict input", () =>
        {
            var text = SeedCodec.Encode(1234);
            foreach (var position in new[] { 0, 3, 5, 8 })
            {
                var corrupt = text.ToCharArray();
                corrupt[position] = SeedCodec.Alphabet[(SeedCodec.Alphabet.IndexOf(corrupt[position]) + 1) % 32];
                True(!SeedCodec.TryDecode(new string(corrupt), out _));
            }
            foreach (var invalid in new string?[] { null, "", "abcdefgh", "ABCD_EFGH", "abcd efgh", "IIII IIII", "\uFFFFBCD EFGH" })
                True(!SeedCodec.TryDecode(invalid, out _));
        });
        Check("10000 seed round trips", () =>
        {
            var mt = new Mt19937(77);
            for (var i = 0; i < 10000; i++)
            { var seed = mt.NextUInt(); True(SeedCodec.TryDecode(SeedCodec.Encode(seed), out var decoded)); Equal(seed, decoded); }
        });
        Check("start seed initialization and next-seed schedule", () =>
        {
            var vector = vectors.Xorshift.Single(v => v.Seed == 1 && v.Shifts.SequenceEqual(new[] { 3, 23, 25 }));
            var state = new StartSeedState(1);
            for (var i = 0; i < 14; i++) Equal(vector.Values[i], state.GetStageSeed(i));
            Equal(vector.Values[14], state.AdditionalSeed); Equal(vector.Values[15], state.NextSeed());
            Throws<ArgumentOutOfRangeException>(() => state.GetStageSeed(-1));
            Throws<ArgumentOutOfRangeException>(() => state.GetStageSeed(14));
        });
        Check("zero start seed consumes one global MT draw", () =>
        {
            var mt = new Mt19937(); var state = new StartSeedState(0, mt);
            Equal(vectors.MtDefaultFirstTen[0], state.StartSeed); Equal(vectors.MtDefaultFirstTen[1], mt.NextUInt());
            Throws<ArgumentException>(() => new StartSeedState(0));
        });
        Check("start seed snapshot replay", () =>
        {
            var state = new StartSeedState(9876); state.NextSeed();
            var saved = RoundTrip(state.Capture()); var restored = StartSeedState.Restore(saved);
            for (var i = 0; i < 100; i++) Equal(state.NextSeed(), restored.NextSeed());
            saved.StageSeeds[0] = 0; True(restored.GetStageSeed(0) != 0);
        });
        Check("pool boundaries, depletion and preserve flag", () =>
        {
            var pool = Pool();
            Equal(1, pool.Select(0, PoolFlags.PreserveWeight)!.Id);
            Equal(2, pool.Select(0.25f, PoolFlags.PreserveWeight)!.Id);
            Equal(3, pool.Select(0.75f, PoolFlags.PreserveWeight)!.Id);
            Equal(1f, pool.Entries[0].RemainingWeight);
            Equal(1, pool.Select(0)!.Id); Equal(0f, pool.Entries[0].RemainingWeight); True(pool.Excluded.Contains(1));
            True(pool.Select(0, eligible: e => e.Id != 1)!.Id != 1);
        });
        Check("pool strict removal threshold", () =>
        {
            var pool = new ItemPool([new(7, 2, 2, 1, 1)]);
            pool.Select(0); Equal(1f, pool.Entries[0].RemainingWeight); True(!pool.Excluded.Contains(7));
            pool.Select(0); Equal(0f, pool.Entries[0].RemainingWeight); True(pool.Excluded.Contains(7));
            True(pool.Select(0) is null);
        });
        Check("pool exhausted, exclusions, item type flags", () =>
        {
            True(new ItemPool([]).Select(0) is null);
            True(new ItemPool([new(1, 0, 0, 0, 0)]).Select(0) is null);
            True(new ItemPool(Pool().Entries, [1, 2, 3]).Select(0.3f) is null);
            var pool = new ItemPool([new(1, 1, 1, 0, 0, 3), new(2, 1, 1, 0, 0, 1)]);
            Equal(2, pool.Select(0, PoolFlags.ExcludeType3AndExtendRepicks)!.Id);
            Equal(1, pool.Select(0.9f, PoolFlags.RequireType3)!.Id);
            True(pool.Select(0, PoolFlags.RequireType3 | PoolFlags.ExcludeType3AndExtendRepicks) is null);
        });
        Check("repick exhaustion fallback wraps and excludes rejected entry", () =>
        {
            var pool = new ItemPool([new(1, 1, 1e-20f, 0, 0), new(2, 1, 1e-20f, 0, 0)]);
            // At 1/3, complement remapping stays inside entry 1 (within float error).
            Equal(2, pool.Select(1f / 3)!.Id);
            var single = new ItemPool([new(1, 1, 0, 0, 0)]);
            True(single.Select(0.5f) is null);
        });
        Check("pool XML schema and validation", () =>
        {
            using var xml = new MemoryStream(Encoding.UTF8.GetBytes("<ItemPools><Pool Name='treasure'><Item Id='7' Weight='2.5' DecreaseBy='0.5' RemoveOn='0.1'/></Pool></ItemPools>"));
            var pool = ItemPool.LoadXml(xml)["treasure"];
            Equal(2.5f, pool.TotalBaseWeight); Equal(7, pool.Select(0)!.Id); Equal(2f, pool.Entries[0].RemainingWeight);
            Throws<ArgumentException>(() => new ItemPool([new(1, float.NaN, 1, 0, 0)]));
            Throws<ArgumentOutOfRangeException>(() => pool.Select(1));
        });
        Check("weighted spawn boundaries and fallback", () =>
        {
            SpawnEntry[] entries = [new(1, 0, 0, 1), new(2, 0, 0, 3)];
            Equal(1, WeightedSpawn.Pick(entries, 0).Type); Equal(2, WeightedSpawn.Pick(entries, 0.25f).Type);
            Equal(1, WeightedSpawn.Pick(entries, 1).Type);
            Equal(1, WeightedSpawn.Pick([new(1, 0, 0, 0)], 0.5f).Type);
        });
        Check("room fit and connection restrictions", () =>
        {
            var occupied = new HashSet<GridCell> { new(6, 6) };
            True(!RoomRestrictions.Fits(new(6, 6), [new(0, 0)], occupied));
            True(!RoomRestrictions.Fits(new(12, 12), [new(1, 0)], occupied));
            True(RoomRestrictions.Fits(new(5, 6), [new(0, 0), new(0, 1)], occupied));
            True(RoomRestrictions.ConnectionEligible(new(5, 6), [new(0, 0)], occupied,
                neighbor => neighbor == new GridCell(6, 6)));
            True(!RoomRestrictions.ConnectionEligible(new(5, 6), [new(0, 0)], occupied,
                _ => false));
        });
        Check("damage queues without changing HP", () =>
        {
            var entity = new Combatant(10);
            True(entity.Hit(new(3, 2, 11, 0))); True(!entity.Hit(new(5, 2, 12, 0)));
            Equal(10f, entity.HitPoints); Equal(3f, entity.Pending.Amount);
            True(entity.Hit(new(2, 0x100000000UL, 12, 0)));
            Equal(0x100000002UL, entity.Pending.Flags);
            Equal(5f, entity.ApplyPending()); Equal(5f, entity.HitPoints); Equal(0, entity.Pending.Events.Count);
            Equal(0f, entity.ApplyPending());
            entity.Pending.AdvanceHostTicks(10); True(entity.Hit(new(20, 2, 11, 0))); entity.ApplyPending(); True(entity.Dead);
        });
        Check("callback rejection retains cooldown mutations", () =>
        {
            var queue = new PendingDamage();
            True(!queue.TryQueue(new(3, 0x42, 1, 7), _ => false));
            Equal(10, queue.Gate2); Equal(7, queue.Gate40); Equal(0, queue.Events.Count);
            queue.AdvanceHostTicks(7); True(!queue.TryQueue(new(3, 2, 1, 0))); True(queue.TryQueue(new(3, 0x40, 1, 7)));
        });
        Check("player TakeDamage dispatch and queue", () =>
        {
            var player = new PlayerCombat();
            var rejected = player.TakeDamage(new(2, 0x40, 1, 5), _ => false);
            True(!rejected.Accepted); Equal(0f, player.Pending.Amount);
            var accepted = player.TakeDamage(new(2, 0x40, 1, 5), _ => true);
            True(accepted.Accepted); Equal(2f, accepted.QueuedAmount); Equal(0x40UL, accepted.QueuedFlags);
        });
        Check("first cooldown mutates even if second gate rejects", () =>
        {
            var queue = new PendingDamage(); queue.TryQueue(new(1, 0x40, 1, 20));
            True(!queue.TryQueue(new(1, 0x42, 1, 5))); Equal(10, queue.Gate2); Equal(20, queue.Gate40);
        });
        Check("enemy directional events and completion", () =>
        {
            var enemy = new EnemyAnimationModel(); enemy.Tick(new()); Equal(EnemyPhase.Idle, enemy.Phase);
            enemy.Tick(new(Shoot: true, TargetX: -4, TargetY: 4)); Equal(AttackDirection.Left, enemy.Direction);
            Sequence(new[] { EnemyCommand.Projectile }, enemy.Tick(new(ShootEvent: true, AnimationFinished: true)));
            Equal(EnemyPhase.Idle, enemy.Phase); Equal(0, enemy.Frames);
            enemy.Tick(new(Shoot: true, TargetY: 10)); Equal(AttackDirection.Down, enemy.Direction);
        });
        Check("enemy priority, summon, leap and scream", () =>
        {
            var enemy = new EnemyAnimationModel(); enemy.Tick(new());
            enemy.Tick(new(Scream: true, Shoot: true)); Equal(EnemyPhase.Scream, enemy.Phase);
            Sequence(new[] { EnemyCommand.ScreamFinished }, enemy.Tick(new(AnimationFinished: true)));
            enemy.Tick(new(Summon: true, ExistingMinions: 2)); Equal(EnemyPhase.Summon, enemy.Phase);
            Equal(2, enemy.Tick(new(ShootEvent: true, ExistingMinions: 2, AnimationFinished: true)).Length);
            enemy.Tick(new(Leap: true)); Equal(EnemyPhase.Leap, enemy.Phase);
            Sequence(new[] { EnemyCommand.LandingEffect }, enemy.Tick(new(LandingEvent: true, AnimationFinished: true)));
        });
        Check("floor invariants over 200 seeds", () =>
        {
            for (uint seed = 1; seed <= 200; seed++)
            {
                var count = 10 + (int)(seed % 55);
                var floor = FloorGenerator.Generate(new(seed, ShiftTriple.Collectible), count);
                Equal(count, floor.Rooms.Length); Equal(count, floor.Rooms.Select(r => r.Cell).Distinct().Count());
                True(floor.Rooms.All(r => r.Cell is >= 0 and < 169));
                Equal(2 * (count - 1), floor.Rooms.Sum(r => floor.Neighbors(r.Cell).Count()));
                var reached = new HashSet<int> { 84 }; var pending = new Queue<int>([84]);
                while (pending.TryDequeue(out var cell)) foreach (var n in floor.Neighbors(cell)) if (reached.Add(n)) pending.Enqueue(n);
                Equal(count, reached.Count); True(floor.DeadEnds().Length >= 3);
                Equal(RoomKind.Boss, floor.Rooms.Single(r => r.Cell == floor.DeadEnds()[0]).Kind);
                foreach (var room in floor.Rooms.Where(r => r.Cell != 84))
                    True(floor.Neighbors(room.Cell).Any(n => floor.Rooms.Single(r => r.Cell == n).Depth == room.Depth - 1));
            }
        });
        Check("floor deterministic generation and bounded failure", () =>
        {
            var a = FloorGenerator.Generate(new(99, ShiftTriple.Wave));
            var b = FloorGenerator.Generate(new(99, ShiftTriple.Wave)); Equal(a.Render(), b.Render());
            Throws<InvalidOperationException>(() => FloorGenerator.Generate(new(1, ShiftTriple.Wave), 10, 9, 1));
        });
        Check("JSON state restore preserves deterministic continuation", () =>
        {
            var rng = new XorShift32(5678, ShiftTriple.Collectible); var pool = Pool();
            pool.Draw(rng); pool.Draw(rng);
            var restoredRng = XorShift32.Restore(RoundTrip(rng.Capture()));
            var restoredPool = ItemPool.Restore(RoundTrip(pool.Capture()));
            for (var i = 0; i < 20; i++) Equal(pool.Draw(rng)?.Id ?? -1, restoredPool.Draw(restoredRng)?.Id ?? -1);
            var queue = new PendingDamage(); queue.TryQueue(new(2, 2, 1, 0)); queue.TryQueue(new(3, 0x40, 2, 4));
            var restoredQueue = PendingDamage.Restore(RoundTrip(queue.Capture()));
            Equal(queue.Amount, restoredQueue.Amount); Equal(queue.Flags, restoredQueue.Flags); Equal(queue.Gate2, restoredQueue.Gate2);
            Sequence(queue.Drain(), restoredQueue.Drain());
            var enemy = new EnemyAnimationModel(); enemy.Tick(new()); enemy.Tick(new(Shoot: true));
            var restoredEnemy = EnemyAnimationModel.Restore(RoundTrip(enemy.Capture()));
            Sequence(enemy.Tick(new(ShootEvent: true)), restoredEnemy.Tick(new(ShootEvent: true)));
            Equal(enemy.Capture(), restoredEnemy.Capture());
        });
        Console.WriteLine($"Verification: {passed} passed, {failed} failed.");
        return failed == 0 ? 0 : 1;
    }

    private static ItemPool Pool() => new([new(1, 1, 1, 1, 0.1f), new(2, 2, 2, 1, 0.1f), new(3, 1, 1, 1, 0.1f)]);
    private static T RoundTrip<T>(T value) => JsonSerializer.Deserialize<T>(JsonSerializer.Serialize(value, Program.Json), Program.Json)!;
    private static void Check(string name, Action action)
    {
        try { action(); passed++; Console.WriteLine("PASS " + name); }
        catch (Exception ex) { failed++; Console.Error.WriteLine("FAIL " + name + ": " + ex.Message); }
    }
    private static void True(bool condition) { if (!condition) throw new InvalidOperationException("Assertion failed."); }
    private static void Equal<T>(T expected, T actual) where T : notnull
    { if (!EqualityComparer<T>.Default.Equals(expected, actual)) throw new InvalidOperationException($"Expected {expected}, got {actual}."); }
    private static void Sequence<T>(IEnumerable<T> expected, IEnumerable<T> actual) => True(expected.SequenceEqual(actual));
    private static void Throws<T>(Action action) where T : Exception
    { try { action(); } catch (T) { return; } throw new InvalidOperationException("Expected " + typeof(T).Name); }
}
