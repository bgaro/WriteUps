# La Réponse de Voris

## Description

Vous rencontrez Mme de Beauvoir qui vous explique vouloir surprendre son mari Jean Sol Partre. Ce dernier est en train d'écrire un livre et a demandé à son ami Voris un titre approprié. Elle a réussi à se procurer un étrange message, qu'elle pense avoir été chiffré par Voris afin de limiter les fuites d'information. Ne sachant quoi faire avec ceci, elle s'est décidée à aller à la séance de spiritualisme du samedi au café littéraire, où elle vous a rencontré aujourd'hui. Par chance, vous connaissez une oracle pouvant peut être vous aider à déchiffrer ce message. Mais, malchance, cette dernière n'est qu'en mesure de chiffrer un message... Dommage, il va falloir réfléchir pour trouver le titre que Voris a proposé à Jean Sol !

---

Format : 404CTF{titre_du_livre}

message chiffré : pvfdhtuwgbpxfhocidqcznupamzsezp

nc challenges.404ctf.fr 31682

## Solution

Comme pour Le jour de l'espace, on se connecte au netcat et on essaye de comprendre comment le chiffrement fonctionne. On remarque cette fois ci que le chiffrement fonctionne en une seule fois. En testant un peu, on se rend compte que le chiffrement fonctionne un peu à la manière du jour de l'espace : chaque index a une clé associé lors de l'incrémentation. Sauf que dans notre cas, nous ne pouvons pas brute-force la clé car ça représenterait 25^31 possibilités. Les clés sont construites de la manière suivante : incrémentation de 1 en partant de 1 jusqu'à l'index de la lettre modifiée puis on comble le reste de la clé avec l'index : exemple avec l'index 4 [1,2,3,4,4...4]. Pour décoder le message nous allons donc reconstruire le message codé petit à petit. Comme nous connaissons chaque clé, nous reconstruisons le message en partant de la fin (en effet, en partant de la fin, les clés sont identiques pour la partie déja solutionée, nous n'avons donc qu'à nous intéresser à l'index actuel et le précédent), nous trouvons chaque lettre en prenant bien soin de conserver la partie déja trouvée. Le programme python `solve.py` solutionne le challenge.

## Flag : `404CTF{lenclumedesjourneesensoleillees}`
