import socket
import time


def main():
    url = "challenges.404ctf.fr"
    port = 31420
    rhino = "~c`°^)"
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((url, port))
    while True:
        time.sleep(0.1)
        data = s.recv(4096).decode()
        if "404CTF" in data:
            break
        nb_rhino = data.count(rhino)  # count the number of rhino
        s.send(str(nb_rhino).encode() + b"\n")

    print(data)


if __name__ == "__main__":
    main()
