import socket
from Cryptodome.Util.number import long_to_bytes
from Cryptodome.Util.number import bytes_to_long
import time
import math


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("challenges.404ctf.fr", 31674))

    time.sleep(0.1)
    data = s.recv(4098).decode()
    print(data)

    ct = int(data.split("l'oracle!:")[1].split("\n")[1].strip(), base=10)
    n = int(data.split("n°")[1].split(" ")[0], base=16)
    e = 0x10001

    flag1 = b"flag{this_is_a_fake_flag_to_test_your_program_very_long_indeed_hahahathis_is_a_fake_flag_to_test_your_program_very_long_indeed_hahaha}"
    ct1 = pow(bytes_to_long(flag1), e, n)
    flag2 = b"flag{this_is_a_fake_flag_to_test_your_program_very_long_indeed_hahahahahahahahahahahathis_is_a_fake_flag_to_test_your_program_very_long_indeed_hahaha}"
    ct2 = pow(bytes_to_long(flag2), e, n)

    s.sendall(f"{ct1}\n".encode())
    time.sleep(0.1)
    data = s.recv(4098).decode()
    print(data.split("\n"))
    m1 = int(data.split("\n")[0].strip())

    s.sendall(f"{ct2}\n".encode())
    time.sleep(0.1)
    data = s.recv(4098).decode()
    print(data.split("\n"))
    m2 = int(data.split("\n")[0].strip())

    a = m1 - bytes_to_long(flag1)
    b = m2 - bytes_to_long(flag2)

    q = math.gcd(a, b)
    print(q)
    print(n % q)
    p = n // q
    d = pow(e, -1, (p - 1) * (q - 1))
    print(long_to_bytes(pow(ct, d, n)))


if __name__ == "__main__":
    main()
