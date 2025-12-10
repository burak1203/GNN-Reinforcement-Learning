def basic_md5(txt: str) -> str:
    """
    Calculates the MD5 hash of a given txt.

    Args:
        txt (str): The txt to calculate the MD5 hash for.

    Returns:
        str: The MD5 hash of the txt as a hexadecimal string.

    Raises:
        None: This function does not raise any exceptions.

    Examples:
        >>> basic_md5("Hello, World!")
        5eb63bbbe01eeed093cb22bb8f5acdc3

    Note:
        The MD5 hash is calculated using the RFC 1321 algorithm.
    """
    message: bytes = txt.encode("utf-8")

    h0: int = 0x67452301
    h1: int = 0xEFCDAB89
    h2: int = 0x98BADCFE
    h3: int = 0x10325476

    result: bytes = b""

    message_length: int = len(message) * 8
    message += b"\x80"

    while len(message) % 64 != 56:
        message += b"\x00"

        message += message_length.to_bytes(8, byteorder="little")

        for i in range(0, len(message), 64):
            chunk: bytes = message[i: i + 64]
            a: int = h0
            b: int = h1
            c: int = h2
            d: int = h3

            for j in range(64):
                if j < 16:
                    f: int = (b & c) | ((~b) & d)
                    g: int = j
                elif j < 32:
                    f = (d & b) | ((~d) & c)
                    g = (5 * j + 1) % 16
                elif j < 48:
                    f = b ^ c ^ d
                    g = (3 * j + 5) % 16
                else:
                    f = c ^ (b | (~d))
                    g = (7 * j) % 16

                temp: int = d
                d = c
                c = b
                b = b + (
                    (
                        a
                        + f
                        + int.from_bytes(chunk[g * 4: g * 4 + 4], byteorder="little")
                    )
                    << (j % 4 * 8)
                )
                a = temp

            h0 = (h0 + a) & 0xFFFFFFFF
            h1 = (h1 + b) & 0xFFFFFFFF
            h2 = (h2 + c) & 0xFFFFFFFF
            h3 = (h3 + d) & 0xFFFFFFFF

        result = (h0 | (h1 << 32) | (h2 << 64) | (h3 << 96)).to_bytes(
            16, byteorder="little"
        )
        result = result.hex()
    return str(result)
