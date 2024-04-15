import ascon


def main():
    clef = bytes.fromhex("00456c6c616e61206427416c2d466172")

    nonce = b"\x00" * 16

    ct = bytes.fromhex(
        "ac6679386ffcc3f82d6fec9556202a1be26b8af8eecab98783d08235bfca263793b61997244e785f5cf96e419a23f9b29137d820aab766ce986092180f1f5a690dc7767ef1df76e13315a5c8b04fb782"
    )

    data = bytes.fromhex("80400c0600000000")

    print(ascon.decrypt(clef, nonce, data, ct))


if __name__ == "__main__":
    main()
