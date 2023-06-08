def main():
    diff_string("gvshnmijdwalablggmejiqvrhkixhns", "hxvlssprmglxnpawxexddmspgkjzkrx")


# dernier tout +1


def gen_key_dict():
    dict = {}
    for i in range(1, 32):
        key = []
        for n in range(1, i + 1):
            key.append(n)

        while len(key) != 31:
            key.append(i)
        dict[i] = key

    return dict


def main():
    init_string = list("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")  # plain init
    result_string = list("gvshnmijdwalablggmejiqvrhkixhns")  # cipher of plain init
    objective_string = list("pvfdhtuwgbpxfhocidqcznupamzsezp")  # cipher objective

    dict_key = gen_key_dict()
    print(dict_key)

    for i in range(len(objective_string)):
        int_string_i = 30 - i

        while result_string[i] != objective_string[i]:
            result_string = list(
                increment_string("".join(result_string), i + 1, dict_key)
            )
            init_string = (
                init_string[:int_string_i]
                + [chr((ord(init_string[int_string_i]) - 97 + 1) % 26 + 97)]
                + init_string[int_string_i + 1 :]
            )
            if i > 0:
                result_string = list(
                    decrement_string("".join(result_string), i, dict_key)
                )
                init_string = (
                    init_string[: int_string_i + 1]
                    + [chr((ord(init_string[int_string_i + 1]) - 97 - 1) % 26 + 97)]
                    + init_string[int_string_i + 2 :]
                )

        print("".join(init_string), "".join(result_string), "".join(objective_string))


def increment_string(str1, n, dict_key):
    str2 = ""
    for i in range(len(str1)):
        str2 += chr(((ord(str1[i]) - 97 + dict_key[n][i]) % 26) + 97)
    return str2


def decrement_string(str1, n, dict_key):
    str2 = ""
    for i in range(len(str1)):
        str2 += chr(((ord(str1[i]) - 97 - dict_key[n][i]) % 26) + 97)
    return str2


def diff_string(str1, str2):
    for i in range(len(str1)):
        print((ord(str2[i]) - ord(str1[i])) % 26)


if __name__ == "__main__":
    main()
