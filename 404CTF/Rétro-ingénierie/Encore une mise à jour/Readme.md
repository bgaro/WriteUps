# Encore une mise à jour !

## Description

« RAAAAAAH !! »

Un cri sourd se fait entendre près du comptoir. Vous vous approchez, curieux. Vous remarquez le propriétaire des lieux fou de rage.

« Encore cette satanée Terreur des Quincailliers, il a volé tout mon café ! Je vais devoir appeler l'inspecteur Blognard. Mais comment diable a-t-il fait ?
Vous ! Là ! Vous êtes la personne qui avez aidé les Hackademitiens toute la journée non ? »

Il vous pointe du doigt.

« Et bien ça tombe parfaitement, j'ai un mystère sur les bras, depuis que j'ai mis à jour mon coffre fort, tout mon café disparait régulièrement ! Je suis convaincu qu'il s'agit d'un des nombreux méfaits de cette fameuse Terreur des Quincailliers, mais l'inspecteur refuse de me croire ! Vous voulez bien me prouver que c'est possible de trouver le mot de passe ? D'ailleurs le vendeur m'avait juré qu'il était inviolable ! Si vous arrivez à prouver le contraire, je vais enfin pouvoir porter plainte !»

---

Pour ce challenge il suffit de trouver le mot de passe qui valide le programme. Attention cepenndant, il ne fonctionne que avec Python 3.11.

## Solution

En prenant connaissance du programme python, on se rend compte qu'il va falloir trouver un mot de passe respectant les conditions énoncées. Les conditions sont organisées de la façon suivante :

- le mot de passe doit faire 48 caractères
- Il y a 64 conditions totales mais on ne doit en respecter que 32 précisément
- Chaque condition possède un doublon qui diffère légèrement (exemple : `dumas[3] + cody * dumas[4] + dumas[5] == 19862` et `dumas[3] + cody * dumas[4] + dumas[5] == 49274`)

Nous allons utiliser la bibliothèque `z3` pour solutionner ce challenge. Pour se faire, nous allons prendre chaque condition ainsi que son doublon, faire un Xor (seule une condition doit être vraie), et ajouter le résultat à une liste. Nous allons demander à `z3` de trouver une solution pour cette liste. Si une solution est trouvée, on l'affiche.

Dans un premier temps, nous définissons les vecteurs de travail de `z3`, il s'agit de vecteurs binaires de taille 24 (j'avais essayé dans un premier temps avec un vecteur de taille 16 mais certaines conditions provoquaient un overflow car la valeur maximale du vecteur était `65535`.)

Ensuite, nous ajoutons une condition pour chaque vecteur afin que la valeur de chaque vecteur soit comprise entre `0` et `255` (car nous voulons des caractères ASCII).

Nous ajoutons ensuite les conditions du programme. Nous faisons une liste `condition` dans laquelle nous ajoutons chaque condition xorée avec son doublon. Nous ajoutons finalement la condition finale qui demande que la somme des vecteurs soit égale à `32`. Le script solution se trouve dans `solve.py`.

## Flag : `404CTf{H!Dd&N-v4r$_f0r_5p3ciaLiz3d_0pCoD3S!|12T5Y22EML8}`
