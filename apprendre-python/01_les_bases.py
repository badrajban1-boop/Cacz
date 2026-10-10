# ==========================================================
# LEÇON 1 : LES BASES
# Lance ce fichier avec :  python3 01_les_bases.py
# Tout ce qui suit un # est un commentaire : Python l'ignore.
# ==========================================================

# --- 1. Afficher du texte ---
print("Bonjour le monde !")

# --- 2. Les variables : une étiquette posée sur une valeur ---
prenom = "Alice"        # str   : du texte (entre guillemets)
age = 25                # int   : un nombre entier
taille = 1.68           # float : un nombre à virgule (avec un point !)
aime_python = True      # bool  : True (vrai) ou False (faux)

print(prenom, age, taille, aime_python)
print(type(age))        # type() indique le type d'une valeur

# --- 3. Les calculs ---
print(7 + 3)    # 10  addition
print(7 - 3)    # 4   soustraction
print(7 * 3)    # 21  multiplication
print(7 / 2)    # 3.5 division (donne toujours un float)
print(7 // 2)   # 3   division entière
print(7 % 2)    # 1   reste de la division (modulo)
print(2 ** 3)   # 8   puissance

# --- 4. Les f-strings : mettre des variables dans du texte ---
print(f"{prenom} a {age} ans et mesure {taille} m.")
print(f"Dans 10 ans, {prenom} aura {age + 10} ans.")

# --- 5. Convertir entre types ---
texte = "42"
nombre = int(texte)          # "42" -> 42
print(nombre + 1)            # 43
print(str(nombre) + "!")     # "42!"  (on ne peut pas faire "42" + 1)

# --- 6. Demander quelque chose à l'utilisateur ---
# input() renvoie TOUJOURS du texte -> il faut convertir si on veut un nombre.
# Enlève les # des 3 lignes suivantes pour essayer :
# nom = input("Comment t'appelles-tu ? ")
# annee = int(input("En quelle année es-tu né·e ? "))
# print(f"Salut {nom}, tu as environ {2026 - annee} ans.")

# À TOI : change les valeurs de prenom et age, relance le fichier.
