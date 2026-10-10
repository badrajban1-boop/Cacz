# ==========================================================
# LEÇON 3 : LES BOUCLES
# ==========================================================

# --- for + range : répéter un nombre de fois ---
for i in range(5):          # i vaut 0, 1, 2, 3, 4 (5 est exclu)
    print("Tour numéro", i)

for i in range(1, 11):      # de 1 à 10
    print(f"7 x {i} = {7 * i}")

# --- for sur du texte : lettre par lettre ---
for lettre in "Python":
    print(lettre)

# --- Accumuler un résultat ---
total = 0
for nombre in range(1, 101):
    total = total + nombre      # on peut aussi écrire : total += nombre
print("Somme de 1 à 100 :", total)   # 5050

# --- while : répéter TANT QUE la condition est vraie ---
compte = 3
while compte > 0:
    print(compte, "...")
    compte -= 1
print("Décollage 🚀")

# --- break : sortir de la boucle ; continue : passer au tour suivant ---
for n in range(1, 20):
    if n % 2 == 0:
        continue            # on saute les nombres pairs
    if n > 9:
        break               # on arrête tout après 9
    print("Impair :", n)

# ATTENTION : un while dont la condition ne devient jamais fausse
# tourne à l'infini. Ctrl+C pour l'arrêter.
