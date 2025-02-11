# On définit une fonction
def helloWorld():
    print("Hello, world!")

# On appelle la fonction (= on s'en sert)
helloWorld()

# On définit une fonction avec des arguments (= ses paramètres de fonctionnement)
def somme(a, b):
    # On utilise les arguments passés à la fonction
    print(a + b)

# On appelle la fonction en lui passant des arguments
somme(4, 7)

# On définit une fonction avec une valeur de retour
def motLong(mot):
    if len(mot) > 7:
        # La fonction renvoie la valeur True
        return True
    return False

# On affiche la valeur de retour de la fonction
print(motLong("chat"))

# Autre exemple d'utilisation de la valeur de retour
if motLong("torttttttue"):
    print("Youpi")
