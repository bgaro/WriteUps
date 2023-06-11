# De la poésie

## Description

Debout dans l'allée, un homme singulier regarde fixement l'imposante horloge qui, d'un vert canard, plonge la rangée de livres dans une ambiance bucolique très agréable. Perturbé par cette étrange figure, vous n'avez même pas remarqué que quelqu'un s'était rapproché de vous.

« Ne faites pas attention à lui, dit la figure à moitié cachée par l'ombre d'une rangée de livres. Il cherche de l'inspiration pour son nouveau poème, et depuis quelque temps, il est fasciné par les chiffres. Je ne sais pas ce qu'il a fait, mais cela lui a complètement retourné le cerveau, il est devenu incompréhensible. »

La voix féminine laissa place à une grande dame à lunette ronde, elle tenait en main un livre fraichement imprimé.

« Vous le connaissez ?

— Bien sûr ! Nous nous échangeons nos poèmes pour les commenter et les améliorer, mais ces dernières semaines il ne me parle presque plus, et je ne comprends rien du tout à ce qu'il m'a donné ! Regardez ça. »

Elle vous tendit le livre pour que vous puissiez l'examiner. La couverture est toute simple, il y a seulement marqué le titre : Être pair ou ne pas l'être.

Cependant, en l'ouvrant, vous vous rendez compte que ce n'est pas un livre, mais une collection d'images ! Christelle remarqua votre mine stupéfaite et ajouta :

« C'est ce que je vous disais, ce n'est pas de la poésie à ce que je sache. »

D'abord étonné, vous devenez curieux et pensif, qu'est-ce que cela peut-il bien-être ? Après quelques secondes passées à feuilleter l'ouvrage, vous vous exclamez :

«Bien sûr !

— Comment ça ? Vous avez une idée de ce que cela peut être ?

— Je pense oui, je crois bien pouvoir le déchiffrer. »

## Solution

En téléchargeant les sources, nous obtenons un fichier zip `poeme.zip` qui contient près de 6000 images de chiffre en résolution `28*28`. Cela nous fait tout de suite penser au célèbre Dataset du Mnist. De plus la description du challenge nous oriente dans cette voie là : `Être pair ou ne pas l'être`. Nous allons donc prendre les 6000 images dans l'ordre, déterminer le chiffre avec un modèle de Machine Learning et récupérer un booléen (pair ou impair). Ensuite nous allons convertir les booléens en 0 et 1 et les concaténer pour obtenir un nombre binaire. Enfin nous allons convertir ce nombre binaire en ASCII pour obtenir le flag. Le script python `solve.py` fait tout cela.

La difficulté du challenge réside dans le fait qu'il faut créer un dataset custom pour être sur de tester les images dans le bon ordre.  
Une fois le message décodé, il faut remodeler un peu le flag pour prendre en compte les erreus de décodage.

## Flag : `404CTF{d#_L4_p03S1e_qU3lqU3_P3u_C0nT3mp0r4in3}`
