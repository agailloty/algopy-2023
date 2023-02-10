# Une fonction nous permet de modulariser du code Python. 
# On encapsule une logique dans une fonction qu'on nomme. 

def add(x, y):
    return x + y

print(add(5, 2))
print(add(5, 8))
print(add(8, 2))
print(add(5, 6))

def mean(valeurs):
    """Cette fonction calcule la moyenne d'une liste de nombre réel
    valeurs doit être de type list, tupe, n'importe quelle séquence.
    """
    N = len(valeurs)
    sum_valeurs = 0
    for val in valeurs:
        sum_valeurs = sum_valeurs + val
    return sum_valeurs / N

ages = [19, 36, 20, 36, 17, 18, 20]
print(mean(ages))
