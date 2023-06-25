# Navi

## Description

En vous installant à une table, sirotant tranquillement une boisson, vous entendez le bruit monter à l’intérieur du café littéraire.

C'est à ce moment qu'une femme vient s'assoir en face de vous. Elle se présente comme étant Simone DE BEAUVOIR. Vous vous étiez déjà rencontrés lors des comités de lecture des éditions Gallimard.

Pendant votre discussion absolument passionnante, la radio du café diffuse une lecture de La ruelle des lutins. C'est à ce moment que son auteur, Alexandre DUMAS, vient se joindre à votre compagnie.

Toutefois, vous remarquez que ce dernier semble intrigué par la narration, pensant qu'elle doit cacher quelque chose...

---

Le fichier est au format .raw, correspondant à des données brutes — on peut également avoir des fichiers sans extension. Ces fichiers peuvent être lus dans des logiciels comme GNU-Radio (un SDR) ou Audacity (ce dernier est plus simple d'utilisation). Port du casque conseillé.

## Solution

On ouvre le fichier `.raw` dans Audacity en laissant les réglages par défaut et on écoute son contenu.

<audio controls>
  <source src="Navi_ori.mp3" type="audio/mp3">
</audio>

On se rend compte qu'il s'agit d'une biographie qui a l'air bien ralentie. On va donc essayer d'accélérer le son. Pour cela, on va utiliser l'effet `Change Speed` dans Audacity et on va doubler la vitesse pour obtenir l'audio original.

<audio controls>
  <source src="Navi_speed.mp3" type="audio/mp3">
</audio>

On se rend compte qu'il y a un autre audio encore plus ralenti par dessus l'audio original. On va donc accéler encore plus le son pour obtenir cet audio. Pour cela, on multiplie par 5 la vitesse.

<audio controls>
  <source src="Navi_speedup.mp3" type="audio/mp3">
</audio>

On entend désormais bien l'autre audio mais il est inversé. Nous appliquons la transformation nécessaire et obtenons le flag. Sur Audacity, il faut aller dans `Effets` > `Inverser sens`.

<audio controls>
  <source src="flag.mp3" type="audio/mp3">
</audio>

On entends : `Le flag en hexadécimal est 34 30 34 43 54 46 7B 31 74 72 30 5F 34 55 78 5F 52 34 64 31 30 2D 66 52 33 71 55 33 4E 63 33 35 7D`

## Flag : `404CTF{1tr0_4Ux_R4d10-fR3qU3Nc35}`
