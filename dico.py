# On récupère le nom et les ingrédients de la pizza
    nomPizza = listePizza[0].strip()
    ingredientsPizza = listePizza[1].strip()

    # On sépare les ingrédients de la pizza d'après le caractère ","
    listeIngredients = ingredientsPizza.split(",")
    # On nettoie toutes les chaînes de caractères d'un coup
    # grâce à la fonction map()
    listeIngredients = list(map(str.strip, listeIngredients))

    # On remplit le dictionnaire des pizzas
    # nomPizza => [listeIngredients]
    dicoPizzas[nomPizza] = listeIngredients

print(dicoPizzas)

# Exercice : afficher tous les noms de pizzas contenant du jambon
