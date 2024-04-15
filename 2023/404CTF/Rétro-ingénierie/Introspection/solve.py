def main():
    with open("introspection", "rb") as f:
        result = f.read()

    # Skip gif
    offset = result.find(b"\x47\x43\x43\x3a") - 4
    len_of_small_array = int.from_bytes(result[offset : offset + 4], "little")
    offset = offset - len_of_small_array

    # Skip Audio
    offset = remove_padding(result, offset)
    offset = offset - 3
    len_of_small_array = int.from_bytes(result[offset : offset + 3], "little")
    offset = offset - len_of_small_array
    # small array
    offset = remove_padding(result, offset)
    offset = offset - 2
    len_of_small_array = int.from_bytes(result[offset : offset + 2], "little")
    offset = offset - len_of_small_array
    small_array = result[offset : offset + len_of_small_array]

    # big array
    offset = remove_padding(result, offset)
    offset = offset - 3
    len_of_big_array = int.from_bytes(result[offset : offset + 3], "little")
    offset = offset - len_of_big_array
    big_array = result[offset : offset + len_of_big_array]

    result = bytearray()
    for i in range(len(big_array)):
        result.append(
            ((-1 + small_array[i % len_of_small_array] + 1 ^ big_array[i]) % 256)
        )

    while result[:4] == b"\x7f\x45\x4c\x46":
        try:
            tmp_result = result
            offset = result.find(b"\x47\x43\x43\x3a") - 4
            len_of_small_array = int.from_bytes(result[offset : offset + 4], "little")

            # Avoid padding
            offset = remove_padding(result, offset)
            small_array = result[offset - len_of_small_array : offset]
            offset = offset - len_of_small_array

            # Avoid padding
            offset = remove_padding(result, offset)

            # 2 cases here, either 2 or 3 bytes for the length of the big array
            len_of_big_array = int.from_bytes(result[offset - 3 : offset], "little")
            # We know that the length of the big array will be smaller than 2601128 (length of the big array in the first iteration)
            if len_of_big_array > 2601128:
                len_of_big_array = int.from_bytes(result[offset - 2 : offset], "little")
                offset = offset - 2
            else:
                offset = offset - 3

            big_array = result[offset - len_of_big_array : offset]

            result = bytearray()
            for i in range(len(big_array)):
                result.append(
                    (
                        (-1 + small_array[i % len_of_small_array] + 1 ^ big_array[i])
                        % 256
                    )
                )
        except Exception as e:
            break
    print(result[:4])
    with open("result", "wb") as f:
        f.write(tmp_result)


def remove_padding(result, offset):
    while result[offset - 1] == 0x00:
        offset = offset - 1
    return offset


if __name__ == "__main__":
    main()
