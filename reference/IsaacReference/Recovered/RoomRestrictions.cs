namespace IsaacReference.Recovered;

public readonly record struct GridCell(int X, int Y)
{
    public bool IsValid => X is >= 0 and < 13 && Y is >= 0 and < 13;
    public static GridCell operator +(GridCell left, GridCell right) => new(left.X + right.X, left.Y + right.Y);
}

// Small, data-driven core of the room predicates at 00910d10/00910dd0.
// The native table contains shape-specific offsets; callers provide those
// offsets instead of pretending this API recovered the complete room catalog.
public static class RoomRestrictions
{
    public static bool Fits(GridCell origin, IEnumerable<GridCell> shapeOffsets,
        ISet<GridCell> occupied, ISet<GridCell>? blocked = null)
    {
        ArgumentNullException.ThrowIfNull(shapeOffsets);
        ArgumentNullException.ThrowIfNull(occupied);
        foreach (var offset in shapeOffsets)
        {
            var cell = origin + offset;
            if (!cell.IsValid || occupied.Contains(cell) || blocked?.Contains(cell) == true)
                return false;
        }
        return true;
    }

    public static bool ConnectionEligible(GridCell origin, IEnumerable<GridCell> shapeOffsets,
        ISet<GridCell> occupied, Func<GridCell, bool> hasDoor, Func<GridCell, bool>? isCurrent = null)
    {
        if (!Fits(origin, shapeOffsets, occupied)) return false;
        if (isCurrent?.Invoke(origin) == true) return false;
        return CardinalNeighbors(origin).Any(n => occupied.Contains(n) && hasDoor(n));
    }

    public static GridCell[] CardinalNeighbors(GridCell cell) =>
        [new(cell.X - 1, cell.Y), new(cell.X, cell.Y - 1),
         new(cell.X + 1, cell.Y), new(cell.X, cell.Y + 1)];
}
