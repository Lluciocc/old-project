#On ajoute a notre projet le module qui gere les nombrcls
# aléatoires 
import random

nombre = random.randint(1, 100)

# On créé une variable de type entier pour la réponse de l'utilisateur
rep = 0
# Tant que la réponse de l'utilisateur n'est pas bonne
while rep!=nombre:
    # Récupérer la réponse de l'utilisateur
    reponse = int(input("Choisit un nombre entre 1 et 100.    "))
    # Si c'était trop haut
    if reponse > nombre:
        # Le dire à l'utilisateur
        print("*********************PLUS PETIT*********************")
    # Si c'était trop bas
    elif reponse < nombre:
        # Le dire à l'utilisateur
        print("*********************PLUS GRAND*********************")
# Dire bravo
    else:
        print("*********************BRAVO*********************")