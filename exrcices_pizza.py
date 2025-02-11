import random


# On ouvre un fichier en lecture
fichier = open("pizzas.txt", "r", encoding="utf8")

# On prépare une liste pour les pizzas
pizzas = []
dicoPizzas = {}

# On lit le fichier ligne par ligne
for ligne in fichier:
    # On ajoute la ligne actuelle à la liste
    pizzas.append(ligne.strip())

# On fait le tour de la liste des pizzas
for pizza in pizzas:
    # On sépare la pizza d'après le caractère ":"
    # Ce qui veut dire qu'on obtient une liste de strings
    # Index 0 : nom de la pizza
    # Index 1 : ingrédients de la pizza
    listePizza = pizza.split(":")
    
    # On récupère le nom et les ingrédients de la pizza
    nomPizza = listePizza[0].strip()
    ingredientsPizza = listePizza[1].strip()

    # On sépare les ingrédients de la pizza d'après le caractère ","
    listeIngredients = ingredientsPizza.split(",")
    # On nettoie toutes les chaînes de caractères d'un coup
    # grâce à la fonction map()
    listeIngredients = list(map(str.strip, listeIngredients))
    dicoPizzas[nomPizza] = listeIngredients

for nom, ingr in dicoPizzas.items():
    if "Jambon" in ingr:
        print(nom)

# Exercice :
# Créer un dictionnaire inversé
# nom d'ingrédient => [pizzas contenant l'ingrédient]

dicoIngredients = {}

# On fait le tour du dico
for nom, ingredients in dicoPizzas.items():
    # On fait le tour des ingrédients de la pizza actuelle
    for ingr in ingredients:
        # Si l'ingrédient n'est pas dans le dico
        if ingr not in dicoIngredients.keys():
            # Ajouter la pizza actuelle au dico avec comme clé l'ingrédient actuel
            dicoIngredients[ingr] = [nom]
        # S'il est dans le dico
        else:
            # Rajouter à la liste la pizza actuelle
            dicoIngredients[ingr].append(nom)
#print(dicoIngredients)

# Exercice :
# Créer une fonction qui demande à l'utilisateur s'il aime un ingrédient
# fonction(ingredient) => True / False
def like(ingredient):
    reponse = input("Est-ce que vous aimez : " + ingredient + " ? ").strip().lower()

    if reponse == "o" or reponse == "oui":
        print("J'ai compris oui")
        return True
    
    print("J'ai compris non")
    return False

ingredientChoisit = random.choice(list(dicoIngredients.keys()))
if like(ingredientChoisit):
    pizzaChoisie = random.choice( dicoIngredients[ingredientChoisit])
    print("j'ai trouver pour vous une pizza : "+ pizzaChoisie)
    
