from z3 import *
import string

# /!\ Ce challenge est conçu pour PYTHON 3.11 !
# Il ne FONCTIONNERA PAS SUR UNE VERSION ANTERIEURE !
# Il a été testé et est fonctionnel sur python 3.11.0 et python 3.11.3 je ne garanti RIEN, sur les autres versions
# Modifiez le fichier à vos risques et périls.... Je ne suis pas responsable.

h = __import__("dis")
dico = {"adaptive": True}

# a = input("Mot de passe : ")
# a = [ord(c) for c in a]


def check(dumas, zola):
    cody = h.Bytecode(check, **dico).dis().count("I")
    carmen = 0

    if dumas[36] + cody * dumas[37] + dumas[38] == 25556:
        carmen += 1
    if dumas[3] + cody * dumas[4] + dumas[5] == 19862:
        carmen += 1
    if dumas[21] + cody * dumas[22] + dumas[23] == 39570:
        carmen += 1
    if dumas[0] + dumas[1] + cody * dumas[2] == 35329:
        carmen += 1
    if dumas[6] + dumas[7] + cody * dumas[8] == 67347:
        carmen += 1
    if dumas[3] + dumas[4] + cody * dumas[5] == 100914:
        carmen += 1
    if dumas[3] + cody * dumas[4] + dumas[5] == 49274:
        carmen += 1
    if dumas[6] + cody * dumas[7] + dumas[8] == 61221:
        carmen += 1
    if dumas[36] + dumas[37] + cody * dumas[38] == 64773:
        carmen += 1
    if dumas[9] + dumas[10] + cody * dumas[11] == 49360:
        carmen += 1
    if dumas[9] + cody * dumas[10] + dumas[11] == 18857:
        carmen += 1
    if dumas[9] + cody * dumas[10] + dumas[11] == 46721:
        carmen += 1
    if dumas[15] + dumas[16] + cody * dumas[17] == 58164:
        carmen += 1
    if dumas[15] + dumas[16] + cody * dumas[17] == 144852:
        carmen += 1
    if dumas[12] + dumas[13] + cody * dumas[14] == 147438:
        carmen += 1
    if dumas[12] + dumas[13] + cody * dumas[14] == 59202:
        carmen += 1
    if dumas[45] + cody * dumas[46] + dumas[47] == 39501:
        carmen += 1
    if dumas[12] + cody * dumas[13] + dumas[14] == 25080:
        carmen += 1
    if dumas[15] + cody * dumas[16] + dumas[17] == 27661:
        carmen += 1
    if dumas[18] + dumas[19] + cody * dumas[20] == 135810:
        carmen += 1
    if dumas[18] + cody * dumas[19] + dumas[20] == 128064:
        carmen += 1
    if dumas[15] + cody * dumas[16] + dumas[17] == 68683:
        carmen += 1
    if dumas[12] + cody * dumas[13] + dumas[14] == 62232:
        carmen += 1
    if dumas[24] + cody * dumas[25] + dumas[26] == 66114:
        carmen += 1
    if dumas[27] + cody * dumas[28] + dumas[29] == 25071:
        carmen += 1
    if dumas[6] + cody * dumas[7] + dumas[8] == 152553:
        carmen += 1
    if dumas[6] + dumas[7] + cody * dumas[8] == 27099:
        carmen += 1
    if dumas[21] + dumas[22] + cody * dumas[23] == 54563:
        carmen += 1
    if dumas[45] + cody * dumas[46] + dumas[47] == 98325:
        carmen += 1
    if dumas[39] + dumas[40] + cody * dumas[41] == 115125:
        carmen += 1
    if dumas[24] + cody * dumas[25] + dumas[26] == 26640:
        carmen += 1
    if dumas[21] + dumas[22] + cody * dumas[23] == 135833:
        carmen += 1
    if dumas[9] + dumas[10] + cody * dumas[11] == 122890:
        carmen += 1
    if dumas[39] + dumas[40] + cody * dumas[41] == 46239:
        carmen += 1
    if dumas[0] + dumas[1] + cody * dumas[2] == 87961:
        carmen += 1
    if dumas[27] + dumas[28] + cody * dumas[29] == 144847:
        carmen += 1
    if dumas[30] + dumas[31] + cody * dumas[32] == 35402:
        carmen += 1
    if dumas[27] + dumas[28] + cody * dumas[29] == 58159:
        carmen += 1
    if dumas[3] + dumas[4] + cody * dumas[5] == 40542:
        carmen += 1
    if dumas[0] + cody * dumas[1] + dumas[2] == 42776:
        carmen += 1
    if dumas[30] + cody * dumas[31] + dumas[32] == 57633:
        carmen += 1
    if dumas[42] + cody * dumas[43] + dumas[44] == 26019:
        carmen += 1
    if dumas[18] + dumas[19] + cody * dumas[20] == 54540:
        carmen += 1
    if dumas[18] + cody * dumas[19] + dumas[20] == 51438:
        carmen += 1
    if dumas[21] + cody * dumas[22] + dumas[23] == 98394:
        carmen += 1
    if dumas[24] + dumas[25] + cody * dumas[26] == 51973:
        carmen += 1
    if dumas[24] + dumas[25] + cody * dumas[26] == 129373:
        carmen += 1
    if dumas[30] + dumas[31] + cody * dumas[32] == 88034:
        carmen += 1
    if dumas[0] + cody * dumas[1] + dumas[2] == 17234:
        carmen += 1
    if dumas[30] + cody * dumas[31] + dumas[32] == 143547:
        carmen += 1
    if dumas[33] + cody * dumas[34] + dumas[35] == 43078:
        carmen += 1
    if dumas[33] + dumas[34] + cody * dumas[35] == 42770:
        carmen += 1
    if dumas[33] + cody * dumas[34] + dumas[35] == 107320:
        carmen += 1
    if dumas[36] + dumas[37] + cody * dumas[38] == 26073:
        carmen += 1
    if dumas[33] + dumas[34] + cody * dumas[35] == 17228:
        carmen += 1
    if dumas[39] + cody * dumas[40] + dumas[41] == 27627:
        carmen += 1
    if dumas[39] + cody * dumas[40] + dumas[41] == 68649:
        carmen += 1
    if dumas[27] + cody * dumas[28] + dumas[29] == 62223:
        carmen += 1
    if dumas[42] + cody * dumas[43] + dumas[44] == 64719:
        carmen += 1
    if dumas[45] + dumas[46] + cody * dumas[47] == 29161:
        carmen += 1
    if dumas[42] + dumas[43] + cody * dumas[44] == 35842:
        carmen += 1
    if dumas[36] + cody * dumas[37] + dumas[38] == 63482:
        carmen += 1
    if dumas[42] + dumas[43] + cody * dumas[44] == 89248:
        carmen += 1
    if dumas[45] + dumas[46] + cody * dumas[47] == 72505:
        carmen += 1

    zola + zola
    return carmen == 32


cody = 518

dumas = [BitVec(f"dumas[{i}]", 24) for i in range(48)]
print(cody)
s = Solver()
for i in range(48):
    s.add(dumas[i] >= 0)
    s.add(dumas[i] <= 255)

conditions = [
    Xor(
        dumas[3] + cody * dumas[4] + dumas[5] == 19862,
        dumas[3] + cody * dumas[4] + dumas[5] == 49274,
    ),
    Xor(
        dumas[9] + cody * dumas[10] + dumas[11] == 46721,
        dumas[9] + cody * dumas[10] + dumas[11] == 18857,
    ),
    Xor(
        dumas[15] + dumas[16] + cody * dumas[17] == 144852,
        dumas[15] + dumas[16] + cody * dumas[17] == 58164,
    ),
    Xor(
        dumas[12] + dumas[13] + cody * dumas[14] == 59202,
        dumas[12] + dumas[13] + cody * dumas[14] == 147438,
    ),
    Xor(
        dumas[12] + cody * dumas[13] + dumas[14] == 62232,
        dumas[12] + cody * dumas[13] + dumas[14] == 25080,
    ),
    Xor(
        dumas[15] + cody * dumas[16] + dumas[17] == 27661,
        dumas[15] + cody * dumas[16] + dumas[17] == 68683,
    ),
    Xor(
        dumas[6] + cody * dumas[7] + dumas[8] == 152553,
        dumas[6] + cody * dumas[7] + dumas[8] == 61221,
    ),
    Xor(
        dumas[6] + dumas[7] + cody * dumas[8] == 67347,
        dumas[6] + dumas[7] + cody * dumas[8] == 27099,
    ),
    Xor(
        dumas[45] + cody * dumas[46] + dumas[47] == 39501,
        dumas[45] + cody * dumas[46] + dumas[47] == 98325,
    ),
    Xor(
        dumas[24] + cody * dumas[25] + dumas[26] == 66114,
        dumas[24] + cody * dumas[25] + dumas[26] == 26640,
    ),
    Xor(
        dumas[21] + dumas[22] + cody * dumas[23] == 54563,
        dumas[21] + dumas[22] + cody * dumas[23] == 135833,
    ),
    Xor(
        dumas[9] + dumas[10] + cody * dumas[11] == 49360,
        dumas[9] + dumas[10] + cody * dumas[11] == 122890,
    ),
    Xor(
        dumas[39] + dumas[40] + cody * dumas[41] == 115125,
        dumas[39] + dumas[40] + cody * dumas[41] == 46239,
    ),
    Xor(
        dumas[0] + dumas[1] + cody * dumas[2] == 35329,
        dumas[0] + dumas[1] + cody * dumas[2] == 87961,
    ),
    Xor(
        dumas[3] + dumas[4] + cody * dumas[5] == 100914,
        dumas[3] + dumas[4] + cody * dumas[5] == 40542,
    ),
    Xor(
        dumas[27] + dumas[28] + cody * dumas[29] == 58159,
        dumas[27] + dumas[28] + cody * dumas[29] == 144847,
    ),
    Xor(
        dumas[18] + dumas[19] + cody * dumas[20] == 135810,
        dumas[18] + dumas[19] + cody * dumas[20] == 54540,
    ),
    Xor(
        dumas[18] + cody * dumas[19] + dumas[20] == 128064,
        dumas[18] + cody * dumas[19] + dumas[20] == 51438,
    ),
    Xor(
        dumas[21] + cody * dumas[22] + dumas[23] == 39570,
        dumas[21] + cody * dumas[22] + dumas[23] == 98394,
    ),
    Xor(
        dumas[24] + dumas[25] + cody * dumas[26] == 129373,
        dumas[24] + dumas[25] + cody * dumas[26] == 51973,
    ),
    Xor(
        dumas[30] + dumas[31] + cody * dumas[32] == 35402,
        dumas[30] + dumas[31] + cody * dumas[32] == 88034,
    ),
    Xor(
        dumas[0] + cody * dumas[1] + dumas[2] == 42776,
        dumas[0] + cody * dumas[1] + dumas[2] == 17234,
    ),
    Xor(
        dumas[30] + cody * dumas[31] + dumas[32] == 57633,
        dumas[30] + cody * dumas[31] + dumas[32] == 143547,
    ),
    Xor(
        dumas[33] + cody * dumas[34] + dumas[35] == 107320,
        dumas[33] + cody * dumas[34] + dumas[35] == 43078,
    ),
    Xor(
        dumas[36] + dumas[37] + cody * dumas[38] == 64773,
        dumas[36] + dumas[37] + cody * dumas[38] == 26073,
    ),
    Xor(
        dumas[33] + dumas[34] + cody * dumas[35] == 42770,
        dumas[33] + dumas[34] + cody * dumas[35] == 17228,
    ),
    Xor(
        dumas[39] + cody * dumas[40] + dumas[41] == 68649,
        dumas[39] + cody * dumas[40] + dumas[41] == 27627,
    ),
    Xor(
        dumas[27] + cody * dumas[28] + dumas[29] == 25071,
        dumas[27] + cody * dumas[28] + dumas[29] == 62223,
    ),
    Xor(
        dumas[42] + cody * dumas[43] + dumas[44] == 26019,
        dumas[42] + cody * dumas[43] + dumas[44] == 64719,
    ),
    Xor(
        dumas[45] + dumas[46] + cody * dumas[47] == 72505,
        dumas[45] + dumas[46] + cody * dumas[47] == 29161,
    ),
    Xor(
        dumas[42] + dumas[43] + cody * dumas[44] == 89248,
        dumas[42] + dumas[43] + cody * dumas[44] == 35842,
    ),
    Xor(
        dumas[36] + cody * dumas[37] + dumas[38] == 25556,
        dumas[36] + cody * dumas[37] + dumas[38] == 63482,
    ),
]
s.add(Sum(*conditions) >= 32)
print(s.assertions())
print("Bravo ! Le flag est 404CTF{le mot de passe que vous avez rentré pour valider}!")

while s.check() == sat:
    result = ""
    for i in range(48):
        result += chr(s.model()[dumas[i]].as_long())
    a = [ord(c) for c in result]
    print(result, check(a, 1))
    print()
