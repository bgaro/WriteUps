def main():
    text1 = """
    Je  reviens   sur notre  discussion
    à propos    de nos romans préférés.
    Pour moi , rien ne vaut  les romans
     français,    Victor    Hugo ,  les
    Misérables         ,   un  drâme en
    plein Paris  . Voilà ce qui me fais
    vibrer. Ou bien  un qui permette de
    s'envoler,quitter notre  Marseille 
    natale      de voyager,  Le   petit
    Prince  de ce  bon vieux   Antoine.
    Mais  toi bien sûr tu  as des goûts
    plus  terre   à terre, quel est ton
    roman  préféré déjà  ? Un auteur du
    Nigéria   racontant  son   enfance.
    Et  pourquoi pas celle d' un auteur
    d'  Allemagne ou     de Finlande  ?
    Soyez   sérieux  mon      ami. Vous
    verrez , et pas dans  10 ans, 15  ,
    22  ou  bien   même  34 non. Dans 5
    à 6  ans tout au   plus. Vous    en
    penserez  la  même chose. Car là où
    vous voyager en  voiture , ou  bien
    même    bateau. Moi   je  suis déjà
    en avion  . Bien  à vous,     on se
    revoit       sous              peu.
    """

    text2 = """
    Je  reviens   sur notre  discussion
    à propos    de nos romans préférés.
    Pour moi , rien ne vaut  les romans
     français,    Victor    Hugo ,  les
    Misérables         ,   un  drâme en
    plein  Paris . Voilà ce qui me fais
    vibrer. Ou bien  un qui permette de
    s'envoler,quitter notre Marseille  
    natale      de voyager,  Le   petit
    Prince  de ce  bon vieux   Antoine.
    Mais  toi bien sûr tu  as des goûts
    plus  terre   à terre, quel est ton
    roman  préféré déjà  ? Un auteur du
    Nigéria   racontant  son   enfance.
    Et  pourquoi pas celle d' un auteur
    d' Allemagne  ou     de  Finlande ?
    Soyez   sérieux  mon      ami. Vous
    verrez , et pas dans 10  ans,  15 ,
    22  ou  bien   même 34  non. Dans 5
    à  6 ans tout au   plus. Vous    en
    penserez  la  même chose. Car là où
    vous voyager en voiture  , ou  bien
    même    bateau. Moi   je  suis déjà
    en  avion . Bien  à vous,     on se
    revoit       sous              peu.
    """

    hidden1 = ""
    hidden2 = ""

    for i in range(len(text1)):
        if text1[i] != text2[i]:
            hidden1 += text1[i]
            hidden2 += text2[i]

    print(hidden1)
    print(hidden2)

    for i in range(len(hidden1) - 1):
        if hidden1[i] == hidden2[i + 1]:
            print(hidden1[i], end="")
    print()
    for i in range(len(hidden1) - 1):
        if hidden2[i] == hidden1[i + 1]:
            print(hidden2[i], end="")


if __name__ == "__main__":
    main()
