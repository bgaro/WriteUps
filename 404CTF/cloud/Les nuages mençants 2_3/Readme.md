# Les nuages menaçants 2/3

## Description

Après avoir trouvé les secrets du nuage, vous les racontez à Proust. Celui-ci vous demande alors d'aller explorer le nuage plus en profondeur.

---

Connectez-vous au nuage avec le mot de passe suivant : 4GqWrNkNuN

Le challenge peut prendre quelques minutes à se lancer.

Le flag est dans /flag.txt.

## Solution

Suite du challenge `Les nuages menaçants 1/3`. En inspectant les secrets nous tombons aussi sur un username et un mot de passe ce qui nous fait penser à des credentials pour se connecter à un service. En décodant les crédentials nous obtenons `user  : proust`, `password : les_nuages` Il nous faut donc trouver une ip avec un port ssh ouvert.  
![creds](./creds.png)

Grâce à la commande `ip a`, nous récupérons l'ip du pod sur lequel nous nous trouvons. En testant les ips proches nous nous rendons compte qu'une d'entre elle à un port ssh ouvert. Pour tester les ips proches, nous utilisons la commande `nmap -p 22 <ip>`.  
![nmap](./nmap.png)

Bingo ! L'adresse 10.42.0.13 possède un port ssh ouvert. Nous nous connectons donc avec les credentials trouvés précédemment. `ssh proust@10.42.0.13`
Avec un `cat /flag.txt` nous obtenons le flag.

## Flag : 404CTF{A_la_Recherche_De_La_Racine}
