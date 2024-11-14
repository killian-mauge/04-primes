"""
Ce module contient des fonctions pour vérifier si un nombre est premier
et pour afficher tous les nombres premiers inférieurs à 100.

Fonctions:
    - isprime(p): Vérifie si un nombre donné est premier.
    - main(): Fonction principale qui affiche les nombres premiers inférieurs à 100.

Usage:
    Ce module peut être exécuté directement pour afficher les nombres premiers
    inférieurs à 100 ou bien les fonctions peuvent être importées dans un autre script.
"""
from math import sqrt

#### Fonction secondaire


def isprime(p):

    # votre code ici
    """

    Vérifie si un nombre est premier.


    Args:

        p: un nombre quelconque

    Returns:

        True ou False

    """
    if p in (1,0):
        return False
    for i in range(2,int(sqrt(p)+1)):
        if p%i == 0:
            return False
    return True

#### Fonction principale


def main():

    # vos appels à la fonction secondaire ici
    """
    Fonction principale qui affiche tous les nombres premiers inférieurs à 100.

    Cette fonction utilise la fonction `isprime` pour vérifier chaque nombre
    entre 0 et 99 et affiche les nombres premiers dans cet intervalle.
    """

    for n in range(100):
        if isprime(n):
            print(n, end=", ")

    print()


if __name__ == "__main__":
    main()
