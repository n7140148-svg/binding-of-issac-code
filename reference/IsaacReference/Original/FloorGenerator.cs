using IsaacReference.Recovered;

namespace IsaacReference.Original;

public enum RoomKind { Start, Normal, Boss, Treasure, Shop }
public sealed record Room(int Cell, int Depth, RoomKind Kind);
public sealed record Floor(Room[] Rooms, int Attempts)
{
    public const int Width = 13;
    public IEnumerable<int> Neighbors(int cell) => FloorGenerator.Neighbors(cell).Where(c => Rooms.Any(r => r.Cell == c));
    public int[] DeadEnds() => Rooms.Where(r => r.Kind != RoomKind.Start && Neighbors(r.Cell).Count() == 1)
        .OrderByDescending(r => r.Depth).ThenBy(r => r.Cell).Select(r => r.Cell).ToArray();

    public string Render()
    {
        var byCell = Rooms.ToDictionary(r => r.Cell);
        return string.Join(Environment.NewLine, Enumerable.Range(0, Width).Select(y =>
            new string(Enumerable.Range(0, Width).Select(x => !byCell.TryGetValue(y * Width + x, out var r) ? '.' :
                r.Kind switch { RoomKind.Start => 'S', RoomKind.Boss => 'B', RoomKind.Treasure => 'T', RoomKind.Shop => '$', _ => '#' }).ToArray())));
    }
}

// Original single-cell tree generator. Uses observed architectural ideas (13x13,
// frontier growth, dead-end sorting), but does not reproduce shape/door selection.
public static class FloorGenerator
{
    public static Floor Generate(XorShift32 rng, int roomCount = 20, int minimumDeadEnds = 3, int maxAttempts = 128)
    {
        if (roomCount is < 4 or > 64) throw new ArgumentOutOfRangeException(nameof(roomCount));
        if (minimumDeadEnds < 1 || minimumDeadEnds >= roomCount) throw new ArgumentOutOfRangeException(nameof(minimumDeadEnds));
        if (maxAttempts < 1) throw new ArgumentOutOfRangeException(nameof(maxAttempts));
        for (var attempt = 1; attempt <= maxAttempts; attempt++)
        {
            var rooms = new List<Room> { new(84, 0, RoomKind.Start) };
            var occupied = new HashSet<int> { 84 };
            var frontier = new LinkedList<int>([84]);
            while (frontier.Count > 0 && rooms.Count < roomCount)
            {
                var cell = frontier.First!.Value;
                frontier.RemoveFirst();
                var candidates = Neighbors(cell).ToArray();
                rng.Shuffle(candidates.AsSpan());
                var budget = cell == 84 ? 2 + (int)rng.NextInt(2) :
                    Math.Max(1, (int)(rng.NextInt(2) + rng.NextInt(2) + rng.NextInt(2) + rng.NextInt(2)));
                foreach (var candidate in candidates)
                {
                    if (occupied.Contains(candidate) || Neighbors(candidate).Count(occupied.Contains) != 1) continue;
                    occupied.Add(candidate);
                    rooms.Add(new(candidate, rooms.First(r => r.Cell == cell).Depth + 1, RoomKind.Normal));
                    if (rng.NextInt(3) == 0) frontier.AddLast(candidate);
                    else frontier.AddFirst(candidate);
                    if (--budget == 0 || rooms.Count == roomCount) break;
                }
            }
            if (rooms.Count != roomCount) continue;
            var floor = new Floor(rooms.ToArray(), attempt);
            var ends = floor.DeadEnds();
            if (ends.Length < minimumDeadEnds) continue;
            var kinds = new[] { RoomKind.Boss, RoomKind.Treasure, RoomKind.Shop };
            for (var i = 0; i < Math.Min(ends.Length, kinds.Length); i++)
            {
                var index = rooms.FindIndex(r => r.Cell == ends[i]);
                rooms[index] = rooms[index] with { Kind = kinds[i] };
            }
            return new Floor(rooms.ToArray(), attempt);
        }
        throw new InvalidOperationException("No floor satisfied the requested constraints within the attempt limit.");
    }

    internal static IEnumerable<int> Neighbors(int cell)
    {
        var x = cell % Floor.Width;
        var y = cell / Floor.Width;
        if (x > 0) yield return cell - 1;
        if (y > 0) yield return cell - Floor.Width;
        if (x < Floor.Width - 1) yield return cell + 1;
        if (y < Floor.Width - 1) yield return cell + Floor.Width;
    }
}
