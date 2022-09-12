def decorateur_tout_neuf(fonction_a_decorer):
    def wrapper_autour_de_la_fonction_originale():
        print("Avant que la fonction ne s'exécute")
        fonction_a_decorer()
        print("Après que la fonction se soit exécutée")

    return wrapper_autour_de_la_fonction_originale


def une_fonction_intouchable():
    print("Je suis une fonction intouchable, on ne me modifie pas !")


une_fonction_intouchable()




@decorateur_tout_neuf
def fonction_intouchable():
    print("Me touche pas !")


fonction_intouchable()
