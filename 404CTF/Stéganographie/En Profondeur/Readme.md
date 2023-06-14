# En Profondeur

## Description

Alors que vous dégustiez une assiette d'oeufs mayo, un homme fait son apparition dans Le Procope. Il prend place à côté de vous et se présente comme étant Monsieur de Valmont. Il vous raconte avoir reçu une lettre étonnante de Madame de Merteuil. Après quelques temps passé à discuter, il vous confie que celle-ci avait accepté un rendez-vous avec lui suite à un pari gagné. Il doutait franchement qu'elle honore sa parole, d'autant qu'elle voyage beaucoup et qu'il n'a pas le permis b lui permettant de la rejoindre n'importe où. Il s'interroge néanmoins sur cette lettre. Pouvez-vous aider de Valmont à voir le message caché derrière celle-ci ?

---

Format : 404CTF{message_caché_chaque_mot_en_minuscule}

## Solution

En ouvrant le fichier `En_Profondeur`, on se rend compte que nous avons deux textes jumeaux avec des petites différences aux niveaux des espaces. En récupérant les différences, on se retrouve avec deux chaînes de caractères :

`'Paris  Marseile AlemagneFinlande  1015  346  voitureavion '`

`' ParisMarseile Alemagne  Finlande10  1534  6voiture  avion'`

Aucune de ces deux chaînes ne valide le challenge. On se rend cependant compte que des mots présentent les mêmes décalages dans les deux chaînes. On les récupère et on obtient deux chaînes en fonction du sens de décalage :

`ParisFinlande156avion` si on prend les caractères identiques avec un décalage de 1 vers la droite entre les deux chaînes. `(texte1[i] == texte2[i+1])`

`Marseile Alemagne1034 voiture` si on prend les caractères identiques avec un décalage de 1 vers la gauche entre les deux chaînes.`(texte1[i+1] == texte2[i])`

On sait que Valmont n'a pas le permis B, on teste donc le flag `Paris_Finlande_15_6_avion` qui valide le challenge.

## Flag : `404CTF{Paris_Finlande_15_6_avion}`
