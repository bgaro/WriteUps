import requests
import time
import string


def aggressive_url_encode(string):
    return "".join("%{:02x}".format(ord(char)) for char in string)


def main():
    url = "https://ddfc.challenges.404ctf.fr/ddfc?expiry=+5000000000&signature="
    sign = "wawF6dC4Hz9g5NyCc37wLiLZdzJEE/wv"
    alpj = "abcdefghijklmnopqrstuvwxyz+/0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(19, len(sign)):
        # for i in range(15):
        for j in range(len(alpj)):
            new_sign = sign[:i] + alpj[j] + sign[i + 1 :]
            r = requests.get(url + new_sign)
            print(new_sign, url + new_sign)
            if "Invalid signature" not in r.text:
                print(r.text)
                return
            else:
                time.sleep(0.5)
                continue


def main2():
    print(ord("y") - ord("C"))
    print(aggressive_url_encode("S"))


if __name__ == "__main__":
    main()


# Valid sign :

# -5625891070 : wawF6dC4Hz9g5NyCc3j1KCDcfztFE/sv
# -5625891079 : wawF6dC4Hz9g5NyCc3j1KCDcfztFE/sm


# -5625891090 : wawF6dC4Hz9g5NyCc3j1KCDcfztFE/Uv
# -5625891080 : wawF6dC4Hz9g5NyCc3j1KCDcfztFE/Qv
# -5625891070 : wawF6dC4Hz9g5NyCc3j1KCDcfztFE/sv
# -5625891060 : wawF6dC4Hz9g5NyCc3j1KCDcfztFE/ov
# -5625891050 : wawF6dC4Hz9g5NyCc3j1KCDcfztFE/kv
# -5625891040 : wawF6dC4Hz9g5NyCc3j1KCDcfztFE/gv
# -5625891030 : wawF6dC4Hz9g5NyCc3j1KCDcfztFE/8v
# -5625891020 : wawF6dC4Hz9g5NyCc3j1KCDcfztFE/4v
# -5625891010 : wawF6dC4Hz9g5NyCc3j1KCDcfztFE/0v
# -5625891000 : wawF6dC4Hz9g5NyCc3j1KCDcfztFE/wv

# -5625891100 : wawF6dC4Hz9g5NyCc3j1KCDcfztFEvwv
# -5625891200 : wawF6dC4Hz9g5NyCc3j1KCDcfztFEfwv

# -5625892000 : wawF6dC4Hz9g5NyCc3j1KCDcfztGE/wv
# -5625890000 : wawF6dC4Hz9g5NyCc3j1KCDcfztEE/wv
# -5625880000 : wawF6dC4Hz9g5NyCc3j1KCDcfzpEE/wv
# -5624880000 : wawF6dC4Hz9g5NyCc3j1KCDdfzpEE/wv
# -5614880000 : wawF6dC4Hz9g5NyCc3j1KCPdfzpEE/wv
# -5514880000 : wawF6dC4Hz9g5NyCc3j1KyPdfzpEE/wv
# -4514880000 : wawF6dC4Hz9g5NyCc3j0KyPdfzpEE/wv
# -1514880000 : wawF6dC4Hz9g5NyCc3jxKyPdfzpEE/wv


# -0614880000 : wawF6dC4Hz9g5NyCc3jwKCPdfzpEE/wv
# -0514880000 : wawF6dC4Hz9g5NyCc3jwKyPdfzpEE/wv
# -0414880000 : wawF6dC4Hz9g5NyCc3jwKiPdfzpEE/wv
# -0614800000 : wawF6dC4Hz9g5NyCc3jwKCPdfzJEE/wv
# -0614000000 : wawF6dC4Hz9g5NyCc3jwKCPddzJEE/wv
# -0610000000 : wawF6dC4Hz9g5NyCc3jwKCPZdzJEE/wv


# -0700000000 : wawF6dC4Hz9g5NyCc3jwKSLZdzJEE/wv
# -0600000000 : wawF6dC4Hz9g5NyCc3jwKCLZdzJEE/wv
# -0500000000 : wawF6dC4Hz9g5NyCc3jwKyLZdzJEE/wv
# -0400000000 : wawF6dC4Hz9g5NyCc3jwKiLZdzJEE/wv
# -0300000000 : wawF6dC4Hz9g5NyCc3jwLSLZdzJEE/wv
# -0000000000 : wawF6dC4Hz9g5NyCc3jwLiLZdzJEE/wv

# +0000000000 : wawF6dC4Hz9g5NyCc37wLiLZdzJEE/wv
# +1000000000 : wawF6dC4Hz9g5NyCc37xLiLZdzJEE/wv
# +5000000000 : wawF6dC4Hz9g5NyCc371LiLZdzJEE/wv
