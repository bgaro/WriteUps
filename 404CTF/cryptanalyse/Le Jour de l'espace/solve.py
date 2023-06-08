def key_finder(str1, str2):
    for i in range(len(str1)):
        print(((ord(str2[i]) - ord("a")) - (ord(str1[i]) - ord("a"))) % 25, end=", ")


def increment_key(str1, modulus_key):
    str1 = list(str1)
    for i in range(len(str1)):
        str1[i] = chr((ord(str1[i]) - ord("a") + modulus_key[i]) % 25 + ord("a"))
    return "".join(str1)


def increment_plain(str1, index):
    str1 = list(str1)
    str1[index] = chr((((ord(str1[index]) - ord("a")) + 1) % 25) + ord("a"))
    return "".join(str1)


def main():
    key = {
        5: [8, 3, 12, 17, 24],
        4: [20, 1, 10, 16, 23],
        3: [18, 2, 7, 15, 22],
        2: [4, 0, 6, 14, 21],
        1: [9, 11, 5, 13, 19],
    }

    cipher = "aaaaa"
    plain = "aaaaa"
    goal = "ppadg"

    # barja -> ueoma
    # velma -> spblb
    # assas -> ppadg
    # sinea -> idtfn

    # Disgusting but it works
    for loop1 in range(25):
        tmp_plain_loop1 = plain
        tmp_cipher_loop1 = cipher
        for loop2 in range(25):
            tmp_plain_loop2 = plain
            tmp_cipher_loop2 = cipher
            for loop3 in range(25):
                tmp_plain_loop3 = plain
                tmp_cipher_loop3 = cipher
                for loop4 in range(25):
                    tmp_plain_loop4 = plain
                    tmp_cipher_loop4 = cipher
                    for loop5 in range(25):
                        if cipher == goal:
                            print(f"plain={plain}")
                            print(f"cipher={cipher}")
                            print(key[5])
                            return
                        plain = increment_plain(plain, 4)
                        cipher = increment_key(cipher, key[5])
                        if cipher == goal:
                            print(f"plain={plain}")
                            print(f"cipher={cipher}")
                            print(key[5])
                            return
                    plain = tmp_plain_loop4
                    cipher = tmp_cipher_loop4
                    plain = increment_plain(plain, 3)
                    cipher = increment_key(cipher, key[4])

                plain = tmp_plain_loop3
                cipher = tmp_cipher_loop3
                plain = increment_plain(plain, 2)
                cipher = increment_key(cipher, key[3])
            plain = tmp_plain_loop2
            cipher = tmp_cipher_loop2
            plain = increment_plain(plain, 1)
            cipher = increment_key(cipher, key[2])

        plain = tmp_plain_loop1
        cipher = tmp_cipher_loop1
        plain = increment_plain(plain, 0)
        cipher = increment_key(cipher, key[1])


if __name__ == "__main__":
    main()
