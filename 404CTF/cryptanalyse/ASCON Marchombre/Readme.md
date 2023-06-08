# ASCON Marchombre

## Description

Cela fait maintenant quelques semaines que vous voyagez avec Salim, mais ce que vous attendez le plus chaque jour ce ne sont plus les palpitantes aventures mais plutôt la poésie marchombre que partage avec vous Salim. Vous avez en effet pris goût à écouter les courts poèmes propres à cette guilde qui vous rappellent les haïkus de votre monde.

Ce soir cependant Salim vous met au défi de déchiffrer le code marchombre qui permet de dissimuler les messages qu'il échange avec Ellana et il vous semble alors reconnaitre un chiffrement pas tout-à-fait inconnu

---

clef : 00456c6c616e61206427416c2d466172

nonce : 0

message chiffré :

ac6679386ffcc3f82d6fec9556202a1be26b8af8eecab98783d08235bfca263793b61997244e785f5cf96e419a23f9b29137d820aab766ce986092180f1f5a690dc7767ef1df76e13315a5c8b04fb782

Données associées : 80400c0600000000

## Solution

On installe le package `ascon` de python et on utilise le script `solve.py` pour déchiffrer le message.

## Flag : `404CTF{V3r5_l4_lum1èr3.}`
