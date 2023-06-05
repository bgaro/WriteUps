# Les nuages menaçants 2/3

## Description

Vous prenez une pause bien méritée et vous vous asseyez à une table. Vous regardez les nuages quand un homme s'approche de vous :

« Vous aussi les nuages vous passionnent ? Je vous proposerai bien une madeleine, mais c'est ma dernière... Mais j'oublie l'essentiel : je suis Marcel Proust. »

Il prend quelques minutes pour contempler les nuages, puis il reprend :

« Les nuages m'ont toujours passionné... J'ai entendu parler d'un nouveau type de nuage récemment, pouvez-vous me donner ses secrets ? »

---

Connectez-vous au nuage avec le mot de passe suivant : 4GqWrNkNuN

Le challenge peut prendre quelques minutes à se lancer.

## Solution

Après s'être connecté au cluster, nous nous rendons compte que nous n'avons pas accès aux commandes de bases kubernetes pour accéder à l'api de manière simple.

Cependant, en explorant un peu la machine, nous repérons le dossier `/var/run/secrets/kubernetes.io/serviceaccount` qui contient un token et un certificat nous permettant de nous connecter à l'api kubernetes.

En affichant les variables d'environnement, nous récupérons l'adresse ip de l'api et pouvons commencer à communiquer avec grâce à la commande `curl -H "Authorization: Bearer $TOKEN" --cacert $CRT https://10.43.0.1/api/v1` (Attention aux " double et pas simple). `CRT` étant le path vers le certificat et `TOKEN` le token jwt récupéré.

Nous nous rendons compte que notre utilisateur a des droits très limités mais en testant les différents endpoints, nous tombons sur `/api/v1/secrets` qui nous permet de lister les secrets du cluster et le flag encodé en base64.  
![flag](./flag.png)

## Flag : 404CTF{Attention_aux_secrets!}
