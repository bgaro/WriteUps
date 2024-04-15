# Les Mystères du cluster de la Comtesse de Ségur [1/2]

## Description

Vous rencontrez la Comtesse de Ségur au Procope. La Comtesse de Ségur a créé une entreprise de vente de livres en ligne en s'aidant du succès de ses livres pour enfants et l'a déployé sur un cluster Kubernetes.

Celle-ci vous explique avoir été victime d'une demande de rançon. En effet, quelqu'un lui a volé ses livres pas encore publiés et menace de les publier sur Internet si elle ne lui paye la rançon demandée.

La Comtesse vous demande d'enquêter sur la manière dont le maître chanteur a pu voler ses livres et vous donne pour cela les informations à sa disposition.

---

Votre mission consiste à exploiter le fichier fourni pour y retrouver les traces du maître chanteur.

---

La 2e partie est en rétro-ingénierie.

## Solution

On télécharge le fichier fourni qui est en fichier zip. En le dézippant, on obtient un dossier avec plusieurs fichiers. Ce dossier correspond à certains dossiers d'une machine linux, on repère notamment les dossiers `/etc`, `/usr`. En plus de ces dossiers, on voit différent fichier de log. En inspectant le fichier `io.kubernetes.cri-o.LogPath`, on se rend compte qu'un dossier `agent.zip` a été téléchargé et qu'il contient un fichier `flag.txt`. En remontant dans l'historique, on récupère l'adresse de téléchargement du fichier : `agent.challenges.404ctf.fr`. On télécharge donc le fichier et on obtient le flag.

## Flag : `404CTF{K8S_checkpoints_utile_pour_le_forensic}`
