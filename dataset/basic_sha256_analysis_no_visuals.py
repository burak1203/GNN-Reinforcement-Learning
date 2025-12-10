def basic_sha256(txt: str) -> None:
    """
    A basic SHA-256 hashing function that processes the input text according to the SHA-256 algorithm.

    Args:
        txt (str): The input text to be hashed.

    Returns:
        None

    Example:
        >>> basic_sha256("Hello, World!")
        dffd6021bb2bd5b0af676290809ec3a53191dd81c7f70a4b28688a362182986f
    """
    import struct

    k: list[int] = [
        0x428A2F98,
        0x71374491,
        0xB5C0FBCF,
        0xE9B5DBA5,
        0x3956C25B,
        0x59F111F1,
        0x923F82A4,
        0xAB1C5ED5,
        0xD807AA98,
        0x12835B01,
        0x243185BE,
        0x550C7DC3,
        0x72BE5D74,
        0x80DEB1FE,
        0x9BDC06A7,
        0xC19BF174,
        0xE49B69C1,
        0xEFBE4786,
        0x0FC19DC6,
        0x240CA1CC,
        0x2DE92C6F,
        0x4A7484AA,
        0x5CB0A9DC,
        0x76F988DA,
        0x983E5152,
        0xA831C66D,
        0xB00327C8,
        0xBF597FC7,
        0xC6E00BF3,
        0xD5A79147,
        0x06CA6351,
        0x14292967,
        0x27B70A85,
        0x2E1B2138,
        0x4D2C6DFC,
        0x53380D13,
        0x650A7354,
        0x766A0ABB,
        0x81C2C92E,
        0x92722C85,
        0xA2BFE8A1,
        0xA81A664B,
        0xC24B8B70,
        0xC76C51A3,
        0xD192E819,
        0xD6990624,
        0xF40E3585,
        0x106AA070,
        0x19A4C116,
        0x1E376C08,
        0x2748774C,
        0x34B0BCB5,
        0x391C0CB3,
        0x4ED8AA4A,
        0x5B9CCA4F,
        0x682E6FF3,
        0x748F82EE,
        0x78A5636F,
        0x84C87814,
        0x8CC70208,
        0x90BEFFFA,
        0xA4506CEB,
        0xBEF9A3F7,
        0xC67178F2,
    ]

    message: bytes = txt.encode("utf-8")
    message_length: int = len(message) * 8
    message += b"\x80"
    while len(message) % 64 != 56:
        message += b"\x00"

    message += struct.pack(">Q", message_length)

    h0 = 0x6A09E667
    h1 = 0xBB67AE85
    h2 = 0x3C6EF372
    h3 = 0xA54FF53A
    h4 = 0x510E527F
    h5 = 0x9B05688C
    h6 = 0x1F83D9AB
    h7 = 0x5BE0CD19

    chunks: list[bytes] = [message[i: i + 64]
                           for i in range(0, len(message), 64)]

    for chunk in chunks:
        w: list[int] = [0] * 64

        for i in range(16):
            w[i] = struct.unpack(">I", chunk[i * 4: i * 4 + 4])[0]

        for i in range(16, 64):
            s0: int = (
                (((w[i - 15] >> 7) | (w[i - 15] << (32 - 7))) & 0xFFFFFFFF)
                ^ (((w[i - 15] >> 18) | (w[i - 15] << (32 - 18))) & 0xFFFFFFFF)
                ^ (w[i - 15] >> 3)
            )
            s1: int = (
                (((w[i - 2] >> 17) | (w[i - 2] << (32 - 17))) & 0xFFFFFFFF)
                ^ (((w[i - 2] >> 19) | (w[i - 2] << (32 - 19))) & 0xFFFFFFFF)
                ^ (w[i - 2] >> 10)
            )
            w[i] = (w[i - 16] + s0 + w[i - 7] + s1) & 0xFFFFFFFF

        a, b, c, d, e, f, g, h = h0, h1, h2, h3, h4, h5, h6, h7

        for i in range(64):
            S1: int = (
                (((e >> 6) | (e << (32 - 6))) & 0xFFFFFFFF)
                ^ (((e >> 11) | (e << (32 - 11))) & 0xFFFFFFFF)
                ^ (((e >> 25) | (e << (32 - 25))) & 0xFFFFFFFF)
            )

            ch: int = (e & f) ^ ((~e) & g)
            temp1: int = h + S1 + ch + w[i] + k[i]

            S0 = (
                (((a >> 2) | (a << (32 - 2))) & 0xFFFFFFFF)
                ^ (((a >> 13) | (a << (32 - 13))) & 0xFFFFFFFF)
                ^ (((a >> 22) | (a << (32 - 22))) & 0xFFFFFFFF)
            )

            maj = (a & b) ^ (a & c) ^ (b & c)
            temp2 = S0 + maj

            h = g
            g = f
            f = e
            e = (d + temp1) & 0xFFFFFFFF
            d = c
            c = b
            b = a
            a = (temp1 + temp2) & 0xFFFFFFFF

        h0 = (h0 + a) & 0xFFFFFFFF
        h1 = (h1 + b) & 0xFFFFFFFF
        h2 = (h2 + c) & 0xFFFFFFFF
        h3 = (h3 + d) & 0xFFFFFFFF
        h4 = (h4 + e) & 0xFFFFFFFF
        h5 = (h5 + f) & 0xFFFFFFFF
        h6 = (h6 + g) & 0xFFFFFFFF
        h7 = (h7 + h) & 0xFFFFFFFF

    # Merge result
    result = (
        struct.pack(">I", h0)
        + struct.pack(">I", h1)
        + struct.pack(">I", h2)
        + struct.pack(">I", h3)
        + struct.pack(">I", h4)
        + struct.pack(">I", h5)
        + struct.pack(">I", h6)
        + struct.pack(">I", h7)
    )

    result = result.hex()
    print(result)
