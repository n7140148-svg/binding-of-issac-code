using System.Globalization;
using System.Text.Json;
using IsaacReference.Original;
using IsaacReference.Recovered;

namespace IsaacReference.Runner;

internal static class Program
{
    internal static readonly JsonSerializerOptions Json = new() { WriteIndented = true, PropertyNameCaseInsensitive = true };

    public static int Main(string[] args)
    {
        try
        {
            switch (args.FirstOrDefault() ?? "help")
            {
                case "verify": return Verification.Run();
                case "demo": Demo(args.Length > 1 ? ParseSeed(args[1]) : 5489); break;
                case "seed" when args.Length == 2:
                    var seed = ParseSeed(args[1]);
                    Console.WriteLine($"{seed}: {SeedCodec.Encode(seed)}");
                    break;
                case "pool" when args.Length is 4 or 5:
                    using (var input = File.OpenRead(args[1]))
                    {
                        var pools = ItemPool.LoadXml(input);
                        if (!pools.TryGetValue(args[2], out var pool)) throw new ArgumentException("Unknown pool name.");
                        var random = new XorShift32(ParseSeed(args[3]), ShiftTriple.Collectible);
                        var count = args.Length == 5 ? int.Parse(args[4], CultureInfo.InvariantCulture) : 10;
                        if (count is < 0 or > 100000) throw new ArgumentOutOfRangeException(nameof(count));
                        for (var i = 0; i < count; i++) Console.WriteLine(pool.Draw(random)?.Id.ToString(CultureInfo.InvariantCulture) ?? "exhausted");
                    }
                    break;
                default:
                    Console.WriteLine("IsaacReference: recovered algorithms and explicitly original gameplay models.");
                    Console.WriteLine("verify | demo [uint-seed] | seed <uint-or-formatted-seed> | pool <xml> <name> <seed> [draws]");
                    return args.Length == 0 || args[0] == "help" ? 0 : 2;
            }
            return 0;
        }
        catch (Exception ex) when (ex is ArgumentException or FormatException or IOException or InvalidOperationException or OverflowException or System.Xml.XmlException)
        {
            Console.Error.WriteLine(ex.Message);
            return 1;
        }
    }

    private static uint ParseSeed(string text)
    {
        if (uint.TryParse(text, NumberStyles.None, CultureInfo.InvariantCulture, out var seed)) return seed;
        if (SeedCodec.TryDecode(text, out seed)) return seed;
        throw new FormatException("Expected a uint seed or an uppercase seed in ABCD EFGH format.");
    }

    private static void Demo(uint seed)
    {
        var rng = new XorShift32(seed, ShiftTriple.Collectible);
        var floor = FloorGenerator.Generate(rng);
        Console.WriteLine($"Reference demo, seed {seed} / {SeedCodec.Encode(seed)}");
        Console.WriteLine("Floor, HP application, and AI scheduling use original reference policies.");
        Console.WriteLine(floor.Render());
        Console.WriteLine($"Rooms: {floor.Rooms.Length}, dead ends: {floor.DeadEnds().Length}, attempts: {floor.Attempts}");
        var pool = new ItemPool([new(1, 1, 1, 1, 0.1f), new(2, 2, 2, 1, 0.1f), new(3, 1, 1, 1, 0.1f)]);
        var items = Enumerable.Range(0, 5).Select(_ => pool.Draw(rng)?.Id).ToArray();
        Console.WriteLine("Pool draws: " + JsonSerializer.Serialize(items));
        var combatant = new Combatant(10);
        combatant.Hit(new(3, 2, 100, 0));
        var gated = combatant.Hit(new(3, 2, 100, 0));
        Console.WriteLine($"Before commit: HP={combatant.HitPoints}, pending={combatant.Pending.Amount}, repeated hit accepted={gated}");
        combatant.ApplyPending();
        Console.WriteLine($"After commit: HP={combatant.HitPoints}");
        var enemy = new EnemyAnimationModel();
        enemy.Tick(new());
        enemy.Tick(new(Shoot: true, TargetX: -10));
        var commands = enemy.Tick(new(ShootEvent: true, AnimationFinished: true));
        Console.WriteLine($"AI commands: {string.Join(", ", commands)}; phase: {enemy.Phase}");
        Console.WriteLine("RNG state: " + JsonSerializer.Serialize(rng.Capture(), Json));
    }
}
