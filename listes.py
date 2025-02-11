# On peut stocker tous types de données dans une liste
couleurs = ["bleu", "rouge", "vert"]
notes = [5.5, 16.0, 10.5]
infos = ["test", 5, 3.2, False]

# On peut créer une liste vide
elements = []

# Affiche "bleu"
print(couleurs[0])

# On ajoute l'élément "jaune" à la liste des couleurs
couleurs.append("jaune")

# On enlève un élément
notes.remove(5.5)

# Affiche le deuxième élément en partant de la fin de la liste
print(couleurs[-2])

# on verifie si un element est present dana la liste
if not "marron" in couleurs:
    print("ya de marrons")