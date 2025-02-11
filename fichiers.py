# on ouvre un fichier de lecture
fichier = open("pizzas.txt" , "r", encoding="utf8")


for ligne in fichier:
    print(ligne.strip())