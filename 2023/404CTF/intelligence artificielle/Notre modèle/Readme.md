# Notre modèle

## Description

Narrativement, ce challenge vient après "De la poésie" et "Le petit chat", cependant il peut être résolu indépendamment des deux autres.
Nous vous conseillons néanmoins de lire l'énoncé des challenges précédants pour comprendre le contexte.
Après avoir passé l'après-midi à déchiffrer la poésie d'Etre pair ou de ne pas l'être, non sans une bonne dizaine de cafés, Christine vous remercia et partit chercher ses affaires. A son retour, une idée lui traversa l'esprit.

« Dites-moi, vous êtes très doué pour résoudre des énigmes. Vous restez ici ? J'ai un ami qui aurait bien besoin de vos talents.

— Je compte rester un peu encore, l'atmosphère est très agréable. Quel est donc le problème de votre ami ?

— Venez. »

Sans même avoir le temps de ramasser vos affaires, elle vous emmena à la rencontre de ce mystérieux ami. En passant entre les tables vous remarquez que le Chat botté tourne dans tous les sens, il a l'air effrayé. Ou pas, il a réussi à rentrer, c'est l'essentiel non ? Vous décidez de le laisser et de continuer d'avancer pour ne pas perdre de vue la silhouette qui vous entraîne aux fin fonds du café.

« Voici Thorn ! »

L'homme, ou plutôt l'ours ou en fait l'homme, on aurait du mal à faire la différence. Avec son énorme dos courbé et ses longues jambes, la chaise sur laquelle il est assis semble pouvoir le casser d'une seconde à l'autre. Voyant que ce dernier n'a même pas daigné lever les yeux de son travail, elle fut obligée de répéter :

« Voici Thorn ! Il ne parle pas beaucoup, mais il est très gentil ne vous inquiétez pas. Il travaille sur des affaires de disparition en ce moment, je pense qu'il aurait bien besoin de votre aide.

— Je suis en plein travail, si vous souhaitez un rendez-vous, consultez mon emploi du temps et venez me revoir plus tard.

— Tu devrais prendre l'air un peu, cette affaire te monte à la tête. Tu as réussi à trouver une preuve ?

— Non, je suis toujours coincé. »

Après de longues secondes d'hésitation, il finit par dire :

« J'ai réussi à établir une connexion entre un supposé Uchida et notre suspect. On sait qu'il travaillait sur une méthode de chiffrement, basée sur le tatouage de réseaux de neurones. J'ai réussi à récupérer un plan de son travail, mais il me manque la clef de chiffrement, il l'a générée aléatoirement et l'a cachée quelque part. On a perquisitionné ses appartements, mais aucune trace de la clef. Je suis coincé.

— Il doit bien y avoir quelque chose, tu peux nous montrer ? »

Christine ramassa un bout de papier et vous le tendit. A première lecture, un simple morceau de programme. Cependant, un détail attire votre attention. A-t-on vraiment besoin de la clef ?

## Solution

Nous avons à disposition deux fichiers, un fichier python contenant un model pytorch et un fichier de poids. En inspectant le fichier python on ne trouve rien de particulier, on se doute donc que le flag a du être caché dans les poids du modèle. On voit qu'une clé `X` a été choisie par l'attaquant avec la fonction `torch.randn`. Sauf qu'aucune fonction de génération n'a été sélectionnée : le tenseur `X` a donc toujours la même valeur. En lisant un peu mieux la description du challenge, un nom peu commun en ressort : `Uchida`. Après quelques recherche on tombe sur le chercheur Yusuke Uchida. Ses travaux portent sur le watermarking de réseau de neurones : cacher un copyright dans un modèle. Notre objectif est donc clair, récupérer le watermark. En continuant nos recherches, nous tombons sur ce papier : `https://arxiv.org/pdf/2103.09274.pdf` qui explique comment récupérer le watermark. Nous avons donc juste à implémenter l'algorithme décrit dans le papier pour récupérer le watermark. La solution se trouve dans le fichier solve.py.

## Flag : `404CTF{P4s_t0uCh3}`
