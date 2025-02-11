compteur = 1
# boucle while = tant que <onditions>
while compteur < 11 :
    print(compteur)
    compteur = compteur + 1
# boucle for  = pour chaque dans ... dans ... 


# Faire le tour d'un dictionnaire
ages = {
    "Bob": 42,
    "Tom": 12,
    "Fred": 47
}

# On récupère les clés du dictionnaire une à une
for cle in ages:
    print(cle)

# On récupère les valeurs du dictionnaire une à une
for valeur in ages.values():
    print(valeur)

# On récupère les paires clé => valeur du dictionnaire
for cle, valeur in ages.items():
    print("Age de l'utilisateur " + cle + " : " + str(valeur))
