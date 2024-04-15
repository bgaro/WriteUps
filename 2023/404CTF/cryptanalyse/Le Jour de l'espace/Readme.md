# Le Jour de l'espace

## Description

Rimbaud vous propose une séance initiatique au Oui-ja dans l'aile mystique du café littéraire (oui, oui, ça existe), vous avez une vision ésotérique :

Alors que vous voyez le texte suivant ueomaspblbppadgidtfn, Rimbaud vous décrit voir un étrange cadre de 50cm de côté, avec des petits carrés de 10cm de côtés, numérotés de 0 à 24 et jetés pêle-mêle sur le sol. Rimbaud n'y comprends rien, mais vous restez obsédé par cette idée, et décidez de résoudre l'énigme.

---

Toutes les informations nécéssaires à la résolution de ce challenge sont présentes dans l'énoncé ci-dessus.

Format : 404CTF{cequevousalleztrouver}

nc challenges.404ctf.fr 31451

## Solution

En nous connectant au netcat, nous nous rendons compte après quelques tests que :

- Le chiffrement fonctionne par bloc de 5 lettres et si le nombre de lettre n'est pas suffisant des `a` sont ajoutés à la fin.
- `aaaaa` est encode en `aaaaa` (pas de chiffrement)
- Nous nous rendons compte que chaque lettre incrémente le message chiffré d'une combinaison particulière et de manière séquentielle. C'est à dire que la différence entre `aaaaa` et `aaaab` est la même que la différence entre `aaaab` et `aaaac` et ainsi de suite.

Après avoir déterminé les 5 clés, il est facile de retrouver le chiffré voulu en testant toutes les combinaisons possibles. Le programme python `solve.py` solutionne le challenge.  
Le flag obtenu est `barjavelmassassinea`. Il faut cependant se rappeler du premier élément repéré. Le flag est donc `404CTF{barjavelmassassine}`

## Flag : `404CTF{barjavelmassassine}`
