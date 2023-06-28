def main():
    with open("introspection", "rb") as f:
        result = f.read()

    # Skip gif
    offset = result.find(b"\x47\x43\x43\x3a") - 4
    len_of_small_array = int.from_bytes(result[offset : offset + 4], "little")
    offset = offset - len_of_small_array

    # Skip Audio
    offset = offset - 16
    len_of_small_array = int.from_bytes(result[offset : offset + 3], "little")
    offset = offset - len_of_small_array

    offset = offset - 4
    len_of_small_array = int.from_bytes(result[offset : offset + 2], "little")
    offset = offset - len_of_small_array
    small_array = result[offset : offset + len_of_small_array]

    offset = offset - 24
    len_of_big_array = int.from_bytes(result[offset : offset + 3], "little")
    offset = offset - len_of_big_array
    big_array = result[offset : offset + len_of_big_array]

    result = bytearray()
    for i in range(len(big_array)):
        result.append(
            ((-1 + small_array[i % len_of_small_array] + 1 ^ big_array[i]) % 256)
        )

    j = 1
    while result[:4] == b"\x7f\x45\x4c\x46":
        try:
            tmp_result = result
            j += 1
            print(j)
            offset = result.find(b"\x47\x43\x43\x3a") - 4
            len_of_small_array = int.from_bytes(result[offset : offset + 4], "little")

            # Avoid padding
            for k in range(100):
                if result[offset - 1] == 0x00:
                    offset = offset - 1
                else:
                    break
            small_array = result[offset - len_of_small_array : offset]
            offset = offset - len_of_small_array

            # Avoid padding
            for k in range(100):
                if result[offset - 1] == 0x00:
                    offset = offset - 1
                else:
                    break
            len_of_big_array = int.from_bytes(result[offset - 3 : offset + 1], "little")
            if len_of_big_array > 2601128:
                len_of_big_array = int.from_bytes(
                    result[offset - 2 : offset + 2], "little"
                )

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
        print(j)


if __name__ == "__main__":
    main()
