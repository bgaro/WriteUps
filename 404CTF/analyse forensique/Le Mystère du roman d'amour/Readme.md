# Le Mystère du roman d'amour

## Description

En train de faire les cent pas dans un couloir du café se trouve Joseph Rouletabille. Il est préoccupé par un mystère des plus intrigants : une de ses amies, qui écrit régulièrement des livres passionnants, a perdu le contenu de son dernier roman !! Elle a voulu ouvrir son oeuvre et son éditeur a crashé... Il semblerait qu'un petit malin a voulu lui faire une blague et a modifié ses fichiers. Elle n'a pu retrouver qu'un seul fichier étrange, que Joseph vous demande de l'aider à l'analyser afin de retrouver son précieux contenu et de comprendre ce qu'il s'est passé.

---

Vous devez retrouver :

le PID du processus crashé
le chemin complet vers le fichier en question (espaces autorisés) : la forme exacte trouvée dans le challenge et la forme étendue commençant par un / permettent toutes les deux de valider le challenge
le nom de l'amie de Rouletabille
le nom de la machine
le contenu TEXTUEL du brouillon de son livre (si vous avez autre chose que du texte, continuez à chercher : vous devez trouver un contenu texte qui ressemble clairement au début d'un roman). Une fois ce contenu trouvé, il sera clairement indiqué quelle partie utiliser pour soumettre le flag (il s'agira d'une chaîne de caractères en leet)
Le flag est la suite de ces éléments mis bout à bout, et séparés par un tiret du 6 (-), le tout enveloppé par 404CTF{...}.

Un exemple de flag valide :

404CTF{1234-/ceci/est/un/Chemin avec/ des espaces1337/fichier.ext-gertrude-monPcPerso-W0w_Tr0P_1337_C3_T3xt3}

Format : 404CTF{PidDuProcessusCrashé-chemin/vers le/fichier-nomUser-nomDeLaMachine-contenuDuFichier}

## Solution

Un fichier `fichier-etange.swp` nous est fourni, il s'agit d'un fichier de swap de Vim. Nous pouvons donc utiliser `vim -r fichier-etrange.swp` pour ouvrir le fichier de swap et récupérer le contenu du fichier qui a été perdu. On se rend compte que le fichier perdu est `~jaqueline/Documents/Livres/404 Histoires d'Amour pour les bibliophiles au coeur d'artichaut/brouillon.txt` :

![vim.png](vim.png)

De plus, en regardant les premiers octets du fichier, on remarque qu'il s'agit d'un fichier `png` :

![png.png](png.png)

Nous sauvegardons donc le fichier sous le nom `brouillon.png` et nous obtenons l'image suivante :

<img src="brouillon.png" alt= "brouillon" width="50%" height="50%">

Cependant, l'image ne contient pas le flag. En passant l'image sur apérisolve, on voit que le flag est caché dans les lsb de l'image :

![lsb.png](lsb.png)

En scannant l'image avec un lecteur de qrcode, on obtient :

```text
Il était une fois, dans un village
rempli d'amour, deux amoureux qui s'aimaient...

Bien joué ! Notre écrivaine va pouvoir
reprendre son chef-d'oeuvre grâce à vous!
Voici ce que vous devez rentrer dans la partie
"contenu du fichier" du flag : 3n_V01L4_Un_Dr0l3_D3_R0m4N
```

Pour récupérer le PID du processus craché, nous exécutons simplement un `vim -r` sans préciser le chemin du fichier.

![pid.png](pid.png)

Nous avons désormais toutes les informations nécessaires pour valider le challenge :

- PID du processus crashé : `168`
- chemin vers le fichier : `~jaqueline/Documents/Livres/404 Histoires d'Amour pour les bibliophiles au coeur d'artichaut/brouillon.txt`
- nom utilisateur `jaqueline`
- nom machine `aime_ecrire`
- contenu du fichier : `3n_V01L4_Un_Dr0l3_D3_R0m4N`

## Flag : `404CTF{168-~jaqueline/Documents/Livres/404 Histoires d'Amour pour les bibliophiles au coeur d'artichaut/brouillon.txt-jaqueline-aime_ecrire-3n_V01L4_Un_Dr0l3_D3_R0m4N}`
