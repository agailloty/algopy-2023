# Les itérations 
# Avec les conditions on peut exécuter un bloc de code que si la ou les conditions sont 
# satisfaites. 
# Avec les itérations on exécuter un même bloc de code plusieurs fois.

# Il faut trouver un moyen de dire à Python combien de fois il doit exécuter le code

# En python si on veut exécuter un bloc de code plusieurs fois on doit parcourir une séquence
# de données, une séquence de donnée peut être une liste, un tuple, un itérateur, générateur

seq = [0, 1, 2, 3, 4, 5, 6, 7]
for i in seq:
    # Exécute le code que je veux
    # Pour chaque valeur dans la séquence fais l'opération suivante
    print("Hello")
    # Je peux récupérer la valeur actuelle
    # La variable d'itération
    print(f"La valeur actuelle est {i}")
    print(f"Le carré de {i} est égal à {i**2} ")