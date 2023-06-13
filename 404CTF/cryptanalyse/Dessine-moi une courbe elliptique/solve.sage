from sage.all import *
import hashlib
from Cryptodome.Cipher import AES
from Cryptodome.Util.number import long_to_bytes,getPrime


p = 231933770389389338159753408142515592951889415487365399671635245679612352781

G_x = 93808707311515764328749048019429156823177018815962831703088729905542530725
G_y = 144188081159786866301184058966215079553216226588404139826447829786378964579
H_x = 139273587750511132949199077353388298279458715287916158719683257616077625421
H_y = 30737261732951428402751520492138972590770609126561688808936331585804316784
cipher = bytes.fromhex("8233d04a29befd2efb932b4dbac8d41869e13ecba7e5f13d48128ddd74ea0c7085b4ff402326870313e2f1dfbc9de3f96225ffbe58a87e687665b7d45a41ac22")
iv = bytes.fromhex("00b7822a196b00795078b69fcd91280d")
field = GF(p)
G_x = field(G_x)
G_y = field(G_y)
H_x = field(H_x)
H_y = field(H_y)
inv = (G_x - H_x)**-1

a = ((G_y**2 - H_y**2)-(G_x**3-H_x**3)) * inv
b = G_y**2 - G_x**3 - a*G_x
print(a)
print(b)
key = str(a) + str(b)
aes = AES.new(hashlib.sha1(key.encode()).digest()[:16], AES.MODE_CBC, iv=iv)
print(aes.decrypt(cipher))

