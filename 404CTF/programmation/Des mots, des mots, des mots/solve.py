import socket

voyelles = "aeiouyAEIOUY"
consonnes = "bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ"


def regle_0(entry):
    return entry


def regle_1(entry):
    return entry[::-1]


def regle_2(entry):
    if len(entry) % 2 == 0:
        return entry[len(entry) // 2 :] + entry[: len(entry) // 2]
    else:
        middle_letter = entry[len(entry) // 2]
        return entry.replace(middle_letter, "")


def get_prec_voy(char):
    if char in voyelles:
        return char
    else:
        return get_prec_voy(chr(ord(char) - 1))


def regle_4(entry):
    list_entry = list(entry)
    entry1 = insert_new_chars(list_entry)
    entry2 = sort_regle_4(entry1)

    return entry2


def sort_regle_4(entry):
    new_dict = {}
    for char in entry:
        if char in new_dict:
            new_dict[char] += 1
        else:
            new_dict[char] = 1

    new_dict = sorted(new_dict.items(), key=lambda x: ord(x[0]))
    new_list = sorted(new_dict, key=lambda x: x[1], reverse=True)

    new_entry = ""
    for element in new_list:
        new_entry += element[0] * element[1]

    return new_entry


def insert_new_chars(list_entry):
    j = 0
    while True:
        for n in range(j, len(list_entry)):
            if list_entry[n] in consonnes:
                vp = ord(get_prec_voy(list_entry[n]))
                s = 0
                for i in range(n - 1, -1, -1):
                    s += (
                        ord(list_entry[i]) * pow(2, n - i) * (list_entry[i] in voyelles)
                    )
                a = ((vp + s) % 95) + 32
                list_entry.insert(n + 1, chr(a))
                j = n + 1
                break
        else:
            break
    return "".join(list_entry)


def regle_3(entry, initial_entry):
    new_entry = initial_entry
    if len(entry) >= 3 and entry[2] in consonnes:
        new_entry = shift_vowels_left(initial_entry)
        new_entry1 = regle_1(new_entry)
        new_entry2 = regle_2(new_entry1)
        new_entry = new_entry2
    else:
        new_entry = shift_vowels_right(initial_entry)
        new_entry1 = regle_1(new_entry)
        new_entry2 = regle_2(new_entry1)
        new_entry = new_entry2

    return new_entry


def shift_vowels_left(entry):
    voy_index = []
    list_entry = list(entry)
    for ind, char in enumerate(entry):
        if char in voyelles:
            voy_index.append(ind)
    if len(voy_index) == 0:
        return entry
    first_voy = list_entry[voy_index[0]]
    for ind in range(len(voy_index) - 1):
        list_entry[voy_index[ind]] = list_entry[voy_index[ind + 1]]
    list_entry[voy_index[-1]] = first_voy
    return "".join(list_entry)


def shift_vowels_right(entry):
    voy_index = []
    list_entry = list(entry)
    for ind, char in enumerate(entry):
        if char in voyelles:
            voy_index.append(ind)

    if len(voy_index) == 0:
        return entry

    last_voy = list_entry[voy_index[-1]]
    for ind in range(len(voy_index) - 2, -1, -1):
        list_entry[voy_index[ind + 1]] = list_entry[voy_index[ind]]
    list_entry[voy_index[0]] = last_voy
    return "".join(list_entry)


def translate(word):
    word1 = regle_1(word)
    word2 = regle_2(word1)
    word3 = regle_3(word2, word)
    word4 = regle_4(word3)
    return word4


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("challenges.404ctf.fr", 30980))

    data = s.recv(1024).decode()
    print(data)
    entry = data.split("Entrée : ")[1].split("\n")[0].strip()
    entry = entry.strip("{").strip("}")

    entry0 = regle_0(entry)
    s.send(entry0.encode() + b"\n")
    print("Sent: " + entry0)

    print(s.recv(4096).decode())

    entry1 = regle_1(entry0)
    s.send(entry1.encode() + b"\n")
    print("Sent: " + entry1)

    print(s.recv(4096).decode())

    entry2 = regle_2(entry1)
    s.send(entry2.encode() + b"\n")
    print("Sent: " + entry2)

    print(s.recv(4096).decode())

    entry3 = regle_3(entry2, entry)
    s.send(entry3.encode() + b"\n")
    print("Sent: " + entry3)

    print(s.recv(4096).decode())

    entry4 = regle_4(entry3)
    s.send(entry4.encode() + b"\n")
    print("Sent: " + entry4)

    data = s.recv(4096).decode()
    new_entry = data.split("Entrée : {")[1].split("}")[0].strip()
    print(new_entry + "\n")
    words = new_entry.split(" ")
    output = ""
    for word in words:
        new_word = translate(word)
        output += new_word + " "
    output = output.strip()
    s.sendall(output.encode() + b"\n")
    print("Sent: " + output)

    print(s.recv(4096).decode())


if __name__ == "__main__":
    main()
