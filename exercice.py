#!/usr/bin/env python
# -*- coding: utf-8 -*-


from typing import List


def convert_to_absolute() -> float:
    nombre = float(input("Entrez un nombre"))
    nombre = abs(nombre)
    return nombre


def use_prefixes() -> List[str]:
    prefixes, suffixes = 'JKLMNOP', 'ack'
    resultat = []
    for prefixe in prefixes:
        nom = prefixe + suffixes
        resultat.append(nom)
    return resultat


def prime_integer_summation() -> int:
    count = 0
    i = -1
    while count < 100:
        i += count
        count += 1
    return i


def factorial(number: int) -> int:
    if number < 2:
        return 1
    else:
        return number*factorial(number-1)


def use_continue():
    i = 0
    for i in range (10):
        i+=1
        if i==5:
            continue
        else:
            print(i)






def main() :
    print(f"La valeur absolue du nombre est {convert_to_absolute()}")

    print(f"La liste des noms générés avec les préfixes est: {use_prefixes()}")

    print(f"La somme des nombres de 0 à 100 est: {prime_integer_summation()}")

    number = 10
    print(f"La factiorelle du nombre {number} est: {factorial(number)}")

    print(f"L'affichage de la boucle est:")
    use_continue()


if __name__ == '__main__':
    main()
