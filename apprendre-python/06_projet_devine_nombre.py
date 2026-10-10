# ==========================================================
# LEÇON 6 : MINI-PROJET — LE JEU DU NOMBRE MYSTÈRE
# L'ordinateur choisit un nombre, tu dois le deviner.
# Réutilise : variables, input, conditions, boucles, fonctions.
# ==========================================================
import random   # import = utiliser un module de la bibliothèque standard


def demander_nombre():
    """Redemande tant que l'utilisateur ne tape pas un nombre valide."""
    while True:
        reponse = input("Ton essai : ")
        if reponse.isdigit():
            return int(reponse)
        print("Ce n'est pas un nombre, réessaie.")


def jouer(maximum=100):
    secret = random.randint(1, maximum)
    essais = 0
    print(f"J'ai choisi un nombre entre 1 et {maximum}. À toi !")

    while True:
        essai = demander_nombre()
        essais += 1
        if essai < secret:
            print("C'est plus ⬆️")
        elif essai > secret:
            print("C'est moins ⬇️")
        else:
            print(f"Bravo 🎉 trouvé en {essais} essais !")
            return essais


# Ce bloc ne s'exécute que si on lance CE fichier directement.
if __name__ == "__main__":
    jouer()

# IDÉES D'AMÉLIORATION (à faire toi-même) :
#  1. Limiter le nombre d'essais à 7 : au-delà, c'est perdu.
#  2. Proposer de rejouer à la fin ("Rejouer ? o/n").
#  3. Garder le meilleur score (le plus petit nombre d'essais).
#  4. Choisir la difficulté : facile (1-10), moyen (1-100), dur (1-1000).
