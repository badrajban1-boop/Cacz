# ==========================================================
# LEÇON 4 : LISTES ET DICTIONNAIRES
# ==========================================================

# --- Les listes : une suite ordonnée de valeurs ---
fruits = ["pomme", "banane", "cerise"]

print(fruits[0])        # "pomme"  (on compte à partir de 0 !)
print(fruits[-1])       # "cerise" (-1 = le dernier)
print(len(fruits))      # 3 éléments

fruits.append("kiwi")   # ajouter à la fin
fruits.remove("banane") # retirer un élément
print(fruits)

print("pomme" in fruits)  # True : est-ce dans la liste ?

for fruit in fruits:
    print("J'aime la", fruit)

# Fonctions utiles sur des listes de nombres
notes = [12, 15, 9, 18, 14]
print("Max :", max(notes), "Min :", min(notes))
print("Moyenne :", sum(notes) / len(notes))
print("Triées :", sorted(notes))

# Construire une nouvelle liste
carres = []
for n in range(1, 6):
    carres.append(n * n)
print(carres)                               # [1, 4, 9, 16, 25]

# Même chose en une ligne (une "compréhension de liste")
carres = [n * n for n in range(1, 6)]
print(carres)

# --- Les dictionnaires : des paires clé -> valeur ---
personne = {"nom": "Alice", "age": 25, "ville": "Lyon"}

print(personne["nom"])          # "Alice"
personne["age"] = 26            # modifier
personne["metier"] = "dev"      # ajouter une clé
print(personne)

for cle, valeur in personne.items():
    print(f"{cle} : {valeur}")

# Exemple classique : compter des éléments
mots = ["chat", "chien", "chat", "poisson", "chat"]
compteur = {}
for mot in mots:
    compteur[mot] = compteur.get(mot, 0) + 1   # get(cle, défaut)
print(compteur)   # {'chat': 3, 'chien': 1, 'poisson': 1}
