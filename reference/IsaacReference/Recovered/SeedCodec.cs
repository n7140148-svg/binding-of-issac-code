namespace IsaacReference.Recovered;

// Evidence: 0093df80 / 0093e080; alphabet bytes at 00b5c940.
public static class SeedCodec
{
    public const string Alphabet = "ABCDEFGHJKLMNPQRSTWXYZ01234V6789";
    private const uint Mask = 0x0fef7ffd;

    public static string Encode(uint seed)
    {
        var value = seed ^ Mask;
        var checksum = Checksum(seed);
        Span<int> digits = stackalloc int[8]
        {
            (int)(value >> 27), (int)(value >> 22 & 31),
            (int)(value >> 17 & 31), (int)(value >> 12 & 31),
            (int)(value >> 7 & 31), (int)(value >> 2 & 31),
            (int)((value & 3) << 3) | checksum >> 5, checksum & 31
        };
        Span<char> output = stackalloc char[9];
        for (var i = 0; i < digits.Length; i++) output[i < 4 ? i : i + 1] = Alphabet[digits[i]];
        output[4] = ' ';
        return new string(output);
    }

    // Native parsing uses zero as its invalid sentinel. This API additionally
    // distinguishes the valid encoded zero from an invalid string.
    public static bool TryDecode(string? text, out uint seed)
    {
        seed = 0;
        if (text is not { Length: 9 } || text[4] != ' ') return false;
        Span<int> digits = stackalloc int[8];
        for (var i = 0; i < digits.Length; i++)
        {
            digits[i] = Alphabet.IndexOf(text[i < 4 ? i : i + 1]);
            if (digits[i] < 0) return false;
        }
        uint payload = 0;
        for (var i = 0; i < 6; i++) payload = (payload << 5) | (uint)digits[i];
        var candidate = ((payload << 2) | (uint)(digits[6] >> 3)) ^ Mask;
        if (Checksum(candidate) != (byte)((digits[6] << 5) | digits[7])) return false;
        seed = candidate;
        return true;
    }

    public static uint DecodeOrZero(string? text) => TryDecode(text, out var seed) ? seed : 0;

    private static byte Checksum(uint seed)
    {
        byte checksum = 0;
        for (; seed != 0; seed >>= 5)
        {
            checksum = unchecked((byte)(checksum + seed));
            checksum = unchecked((byte)((checksum << 1) | (checksum >> 7)));
        }
        return checksum;
    }
}
