# ==========================================================
# LEÇON 5 : LES FONCTIONS
# Une fonction = un bout de code réutilisable, avec un nom.
# ==========================================================

# --- Définir puis appeler ---
def dire_bonjour():
    print("Bonjour !")

dire_bonjour()
dire_bonjour()

# --- Avec des paramètres ---
def saluer(prenom):
    print(f"Salut {prenom} !")

saluer("Alice")
saluer("Karim")

# --- return : la fonction RENVOIE un résultat ---
# print affiche, return donne une valeur qu'on peut réutiliser.
def carre(x):
    return x * x

resultat = carre(4)
print(resultat)              # 16
print(carre(3) + carre(4))   # 25

# --- Plusieurs paramètres et valeur par défaut ---
def prix_ttc(prix_ht, tva=0.20):
    return prix_ht * (1 + tva)

print(prix_ttc(100))         # 120.0 (tva par défaut)
print(prix_ttc(100, 0.055))  # 105.5

# --- Une fonction qui utilise if et une boucle ---
def est_premier(n):
    """Renvoie True si n est un nombre premier."""
    if n < 2:
        return False
    for diviseur in range(2, n):
        if n % diviseur == 0:
            return False     # return arrête la fonction immédiatement
    return True

premiers = [n for n in range(1, 30) if est_premier(n)]
print("Nombres premiers < 30 :", premiers)

# Conseil : une bonne fonction fait UNE chose et a un nom clair.
