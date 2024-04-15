# La Réponse de Voris

## Description

Vous rencontrez Mme de Beauvoir qui vous explique vouloir surprendre son mari Jean Sol Partre. Ce dernier est en train d'écrire un livre et a demandé à son ami Voris un titre approprié. Elle a réussi à se procurer un étrange message, qu'elle pense avoir été chiffré par Voris afin de limiter les fuites d'information. Ne sachant quoi faire avec ceci, elle s'est décidée à aller à la séance de spiritualisme du samedi au café littéraire, où elle vous a rencontré aujourd'hui. Par chance, vous connaissez une oracle pouvant peut être vous aider à déchiffrer ce message. Mais, malchance, cette dernière n'est qu'en mesure de chiffrer un message... Dommage, il va falloir réfléchir pour trouver le titre que Voris a proposé à Jean Sol !

---

Format : 404CTF{titre_du_livre}

message chiffré : pvfdhtuwgbpxfhocidqcznupamzsezp

nc challenges.404ctf.fr 31682

## Solution

Comme pour Le jour de l'espace, on se connecte au netcat et on essaye de comprendre comment le chiffrement fonctionne. On remarque cette fois ci que le chiffrement fonctionne en une seule fois. En testant un peu, on se rend compte que le chiffrement fonctionne un peu à la manière du jour de l'espace : lorsque l'on incrémente une lettre du texte en clair, nous ajoutons à tout le texte chiffré sa clé associée. Sauf que dans notre cas, nous ne pouvons pas brute-force la clé car cela représenterait 25^31 possibilités. Les clés sont construites de la manière suivante : Soit `n` la longueur du texte en clair, lorsque l'on incrémente la lettre `n-i` du texte en clair on ajoute au texte chiffré la clé `[1,2,3...,i+1,i+1,...i+1]` (en supposant dans l'exemple que `i` est strictement supérieur à 2).

Exemple si l'on incrémente la lettre `n-3` du texte en clair, on ajoute au texte chiffré la clé `[1,2,3,4,4,4,4...,4]`.

Nous remarquons donc qu'une partie de la clé reste identique si nous modifions le texte en clair en partant de la fin. Notre mode de fonctionnement va donc être le suivant. Nous allons incrémenter la lettre `n-i` du texte en clair pour retrouver la lettre `i` du texte chiffré en prenant bien soin de conserver la partie déja solutionnée en décrémentant la lettre `n-i + 1` du texte en clair.

On suppose que nous avons déja trouvé les lettres `0` et `1` du texte chiffré, nous travaillons donc sur la lettre `n-2` du texte en clair.

clé `n-2` : `[1,2,3,3,3,3,3...,3]`

clé `n-1` : `[1,2,2,2,2,2,2...,2]`

A chaque incrémentation de la lettre `n-2`, nous allons ajouter à notre texte chiffré la clé correspondante et décrémenter la lettre `n-1` pour soustraire la clé associée au texte chiffré. Ce procédé permet de conserver les deux premières lettres déja trouvées (`+1-1` pour la première, `+2-2` pour la seconde) tout en incrémentant de 1 la lettre `2` du texte chiffré (`+3 -2`). De ce fait, nous pouvons donc retrouver la lettre voulue.

Exemple d'exécution :

```text
objective : pvfdhtuwgbpxfhocidqcznupamzsezp
plaintext=aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaj ciphertext=pebqwvrsmfjujkuppvnsrzeaqtrgqwb
plaintext=aaaaaaaaaaaaaaaaaaaaaaaaaaaaars ciphertext=pvshnmijdwalablggmejiqvrhkixhns
plaintext=aaaaaaaaaaaaaaaaaaaaaaaaaaaanes ciphertext=pvfuazvwqjnynoyttzrwvdieuxvkuaf
plaintext=aaaaaaaaaaaaaaaaaaaaaaaaaaajees ciphertext=pvfdjiefzswhwxhcciafemrndgetdjo
plaintext=aaaaaaaaaaaaaaaaaaaaaaaaaaylees ciphertext=pvfdhgcdxqufuvfaagydckplbecrbhm
plaintext=aaaaaaaaaaaaaaaaaaaaaaaaanllees ciphertext=pvfdhtpqkdhshisnntlqpxcyorpeouz
plaintext=aaaaaaaaaaaaaaaaaaaaaaaafillees ciphertext=pvfdhtuvpimxmnxssyqvuchdtwujtze
plaintext=aaaaaaaaaaaaaaaaaaaaaaabeillees ciphertext=pvfdhtuwqjnynoyttzrwvdieuxvkuaf
plaintext=aaaaaaaaaaaaaaaaaaaaaaqleillees ciphertext=pvfdhtuwgzdodeojjphmltyuknlakqv
plaintext=aaaaaaaaaaaaaaaaaaaaacoleillees ciphertext=pvfdhtuwgbfqfgqllrjonvawmpncmsx
plaintext=aaaaaaaaaaaaaaaaaaaaksoleillees ciphertext=pvfdhtuwgbpapqavvbtyxfkgwzxmwch
plaintext=aaaaaaaaaaaaaaaaaaaxnsoleillees ciphertext=pvfdhtuwgbpxmnxssyqvuchdtwujtze
plaintext=aaaaaaaaaaaaaaaaaatensoleillees ciphertext=pvfdhtuwgbpxfgqllrjonvawmpncmsx
plaintext=aaaaaaaaaaaaaaaaabsensoleillees ciphertext=pvfdhtuwgbpxfhrmmskpowbxnqodnty
plaintext=aaaaaaaaaaaaaaaaxesensoleillees ciphertext=pvfdhtuwgbpxfhojjphmltyuknlakqv
plaintext=aaaaaaaaaaaaaaateesensoleillees ciphertext=pvfdhtuwgbpxfhocciafemrndgetdjo
plaintext=aaaaaaaaaaaaaagneesensoleillees ciphertext=pvfdhtuwgbpxfhocioglksxtjmkzjpu
plaintext=aaaaaaaaaaaaaprneesensoleillees ciphertext=pvfdhtuwgbpxfhocidvazhmiybzoyej
plaintext=aaaaaaaaaaaavurneesensoleillees ciphertext=pvfdhtuwgbpxfhocidqvuchdtwujtze
plaintext=aaaaaaaaaaahourneesensoleillees ciphertext=pvfdhtuwgbpxfhocidqcbjokadbqagl
plaintext=aaaaaaaaaayjourneesensoleillees ciphertext=pvfdhtuwgbpxfhocidqczhmiybzoyej
plaintext=aaaaaaaaagsjourneesensoleillees ciphertext=pvfdhtuwgbpxfhocidqcznsoehfuekp
plaintext=aaaaaaaacesjourneesensoleillees ciphertext=pvfdhtuwgbpxfhocidqcznuqgjhwgmr
plaintext=aaaaaaazdesjourneesensoleillees ciphertext=pvfdhtuwgbpxfhocidqcznupfigvflq
plaintext=aaaaaavedesjourneesensoleillees ciphertext=pvfdhtuwgbpxfhocidqcznupadbqagl
plaintext=aaaaajmedesjourneesensoleillees ciphertext=pvfdhtuwgbpxfhocidqcznupamkzjpu
plaintext=aaaapumedesjourneesensoleillees ciphertext=pvfdhtuwgbpxfhocidqcznupamzoyej
plaintext=aaaelumedesjourneesensoleillees ciphertext=pvfdhtuwgbpxfhocidqcznupamzscin
plaintext=aacclumedesjourneesensoleillees ciphertext=pvfdhtuwgbpxfhocidqcznupamzsekp
plaintext=apnclumedesjourneesensoleillees ciphertext=pvfdhtuwgbpxfhocidqcznupamzseze
plaintext=lenclumedesjourneesensoleillees ciphertext=pvfdhtuwgbpxfhocidqcznupamzsezp
```

## Flag : `404CTF{lenclumedesjourneesensoleillees}`
