# Oracle cassé

## Description

Cette description fait référence à un challenge de l'édition précédente qu'il n'est absolument pas nécessaire de connaître pour faire ce challenge.
Communiqué de la direction du 404CTF
Nous souhaitons prendre la parole pour vous dire que nous avons compris vos plaintes concernant les oracles de l'édition précédente. Nous comprenons que ces derniers ont été jugés injustes et trop difficiles à deviner, et c'est pourquoi nous avions décidé de les retirer. C'est pourquoi nous avons décidé de refaire un nouvel oracle, avec les toutes dernières technologies d'optimisation à notre disposition. Afin de nous excuser pour la gène occasionnée, nous offrons aux 1000 premiers arrivés un cadeau à récupérer directement dans l'oracle. Par souci de transparence, nous vous fournirons cette fois-ci le code de fonctionnement exact de cet oracle.

Nous vous prions d'agréer, Madame, Monsieur, l'expression de nos salutations distinguées.
Colette, directrice du Matin et du 404CTF

---

Toutes les informations neécessaires à la résolution de ce challenge sont présentes dans l'énoncé ci-dessus.

nc challenges.404ctf.fr 31674

## Solution

Probablement le meilleur challenge que j'ai réussi de ce ctf. Nous avons affaire avec un oracle de déchiffrement rsa mais avec une mauvaise implémentation. En effet, l'oracle implémente la méthode RSA CRT (pour Chinese Remainder Theorem) avec le mauvais inverse. Dans notre cas nous avons l'inverse de p modulo q alors que nous aurions voulu l'inverse de q modulo p.

De ce fait, la décryption ne peut se faire. Cependant, nous pouvons utiliser le fait que nous avons tous les paramètres pour chiffrer un message en connaissant sa valeur déchiffrée. En effet nous pouvons retrouver q en faisant la différence entre deux messages `m` et `m_crt`. `m` représente le vrai message décodé et `m_crt` le message décodé avec l'oracle cassé.

En effet, nous avons :

- `m_crt = (m2 + (pinv * (m1-m2) mod(p)) * q) mod(n)`
- `m = (m2 + (qinv * (m1-m2) mod(p)) * q) mod(n)`  
  et donc :
- `m_crt - m = (pinv - qinv) * (m1-m2) * q mod(n)`

En faisant cette opération pour plusieurs messages (au minimum 2), nous pouvons retrouver `q` avec un simple pgcd. nous retrouvons ensuite `p` avec `p = n/q`. Le programme python `solve.py` solutionne le challenge.

## Flag : `404CTF{Un_0r4cl3_vr41m3n7_c4553_c3773_f015}`
