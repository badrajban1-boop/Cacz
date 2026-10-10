# ==========================================================
# Correcteur automatique des exercices.
#   python3 verifier.py            -> vérifie exercices.py
#   python3 verifier.py solutions  -> vérifie solutions.py
# ==========================================================
import importlib
import sys

TESTS = {
    "double": [((4,), 8), ((0,), 0), ((-3,), -6)],
    "est_majeur": [((18,), True), ((17,), False), ((40,), True)],
    "mention": [((17,), "Très bien"), ((14,), "Bien"), ((12.5,), "Assez bien"),
                ((10,), "Passable"), ((3,), "Insuffisant")],
    "somme_jusqua": [((4,), 10), ((100,), 5050), ((1,), 1)],
    "compter_voyelles": [(("bonjour",), 3), (("python",), 2), (("rhm",), 0)],
    "moyenne": [(([10, 20],), 15), (([12, 15, 9],), 12), (([7],), 7)],
    "garder_pairs": [(([1, 2, 3, 4],), [2, 4]), (([1, 3],), []), (([],), [])],
    "compter_mots": [(("le chat et le chien",), {"le": 2, "chat": 1, "et": 1, "chien": 1}),
                     (("a a a",), {"a": 3})],
    "fizzbuzz": [((15,), "FizzBuzz"), ((9,), "Fizz"), ((10,), "Buzz"), ((7,), "7")],
    "inverser": [(("abc",), "cba"), (("Python",), "nohtyP"), (("",), "")],
}


def main():
    nom_module = sys.argv[1] if len(sys.argv) > 1 else "exercices"
    module = importlib.import_module(nom_module)
    reussis = 0

    for nom, cas in TESTS.items():
        fonction = getattr(module, nom)
        erreur = None
        for args, attendu in cas:
            try:
                obtenu = fonction(*args)
            except Exception as e:
                erreur = f"{nom}{args} a planté : {type(e).__name__}: {e}"
                break
            if obtenu != attendu:
                erreur = f"{nom}{args} -> {obtenu!r}, attendu {attendu!r}"
                break
        if erreur:
            print(f"❌ {erreur}")
        else:
            print(f"✅ {nom}")
            reussis += 1

    print(f"\nScore : {reussis}/{len(TESTS)}")
    if reussis == len(TESTS):
        print("Bravo, tout est juste ! 🎉")


if __name__ == "__main__":
    main()
