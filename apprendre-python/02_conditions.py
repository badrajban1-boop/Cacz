# ==========================================================
# LEÇON 2 : LES CONDITIONS
# ==========================================================

# --- Comparaisons : elles donnent True ou False ---
print(5 > 3)     # True
print(5 == 3)    # False  (== compare, = affecte !)
print(5 != 3)    # True   (différent)
print(5 <= 5)    # True

# --- if / elif / else ---
# L'INDENTATION (4 espaces) indique ce qui est "dans" le if.
temperature = 18

if temperature > 25:
    print("Il fait chaud ☀️")
elif temperature > 15:
    print("Il fait doux 🌤️")
else:
    print("Il fait froid ❄️")

# --- Combiner : and, or, not ---
age = 20
a_un_billet = True

if age >= 18 and a_un_billet:
    print("Tu peux entrer.")

jour = "samedi"
if jour == "samedi" or jour == "dimanche":
    print("C'est le week-end !")

if not a_un_billet:
    print("Va acheter un billet.")

# --- Exemple : pair ou impair ? ---
n = 7
if n % 2 == 0:
    print(f"{n} est pair")
else:
    print(f"{n} est impair")

# À TOI : change temperature et n, et prédis le résultat avant de lancer.
