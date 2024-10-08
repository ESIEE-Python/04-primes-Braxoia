"""
Ce module contient deux fonctions principales :

1. est_premier(p) : Vérifie si un nombre est premier.
2. main() : Affiche tous les nombres premiers inférieurs à 100.

Ce programme est un exemple simple de vérification de nombres premiers.
"""

from math import isqrt

#### Fonction secondaire

def est_premier(p):
    """
    Détermine si un nombre est premier.

    Args:
        p (int): Le nombre à vérifier.

    Returns:
        bool: True si le nombre est premier, False sinon.
    """
    if p < 2:
        return False

    for i in range(2, isqrt(p) + 1):
        if p % i == 0:
            return False

    return True

#### Fonction principale

def main():
    """
    Affiche tous les nombres premiers inférieurs à 100.

    Cette fonction parcourt les nombres de 0 à 99 et affiche
    ceux qui sont premiers en utilisant la fonction est_premier.
    """
    for n in range(100):
        if est_premier(n):
            print(n, end=", ")

    print()


if __name__ == "__main__":
    main()
