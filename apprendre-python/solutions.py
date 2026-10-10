# ==========================================================
# SOLUTIONS — à regarder seulement après avoir essayé !
# Vérifier les solutions :  python3 verifier.py solutions
# ==========================================================

def double(x):
    return x * 2


def est_majeur(age):
    return age >= 18


def mention(note):
    if note >= 16:
        return "Très bien"
    elif note >= 14:
        return "Bien"
    elif note >= 12:
        return "Assez bien"
    elif note >= 10:
        return "Passable"
    else:
        return "Insuffisant"


def somme_jusqua(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total


def compter_voyelles(texte):
    compte = 0
    for lettre in texte:
        if lettre in "aeiouy":
            compte += 1
    return compte


def moyenne(nombres):
    return sum(nombres) / len(nombres)


def garder_pairs(nombres):
    return [n for n in nombres if n % 2 == 0]


def compter_mots(phrase):
    compteur = {}
    for mot in phrase.split():
        compteur[mot] = compteur.get(mot, 0) + 1
    return compteur


def fizzbuzz(n):
    if n % 15 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return str(n)


def inverser(texte):
    resultat = ""
    for lettre in texte:
        resultat = lettre + resultat
    return resultat
