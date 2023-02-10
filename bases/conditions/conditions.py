# De base Python exécute toutes les lignes de code du début jusqu'à la fin

print("Cette ligne de code va s'exécuter !")

# Mais des fois nous voulons qu'un bloc de code ne s'exécute que si une ou plusieurs conditions sont remplies
# On utilise le condition if en Python

# On donne une expression que Python va évaluer
# Si l'expression retourne la valeur True alors le code va s'exécucter, si elle retourne
# False alors le code ne s'exécute pas. 

# On utilise les comparateurs logiques pour évaluer la condition

print("10 > 20", 10 > 20)
print("20 > 10", 20 > 10)

# Il existe plusieurs opérateurs pour évaluer des expressions en Python 

print("10 + 30 == 40", 10 + 30 == 40) # L'opérateur == teste l'égalité de deux expressions
print("10 + 30 != 50", 10 + 30 != 50) # L'opérateur != teste la non-égalité de deux expressions

# Pour que le bloc de condition s'exécute, il faut que l'expression évaluée retourne True

if 10 + 20 == 30:
    print("L'expression 10 + 30 = 30")

if 10 + 20 > 30:
    print("Cette ligne de code s'affiche si 10 + 20 > 30")

if 10 + 20 >= 30:
    print("Cette ligne de code s'affiche si 10 + 20 >= 30")

# Jusque là on ne vérifie qu'une seule condition

age = 18
statut = "majeur"

# Il faut que toutes les conditions soient égales à True pour que le code s'exéute
if age >= 18 and statut == "majeur":
    print("L'age est supérieur ou égal à 18 et le statut est majeur")

# L'arithmétique des booléens

print("L'expression True and True s'évalue à : ", True and True)
print("L'expression True and True and True s'évalue à : ", True and True and True)
print("L'expression True and True and True and False s'évalue à : ", True and True and True and False)

print("L'expression False and False s'évalue à : ", False and False)
print("L'expression False or False s'évalue à : ", False or False)
print("L'expression False or True s'évalue à : ", False or True)

# Lorsqu'on passe plusieurs conditions au bloc if il y a l'arithméque des booléens qui s'applique. 


# Un autre cas d'usage c'est d'exécuter d'autre bloc de code si une ou plusieurs conditions
# ne sont pas satisfaites

# Il est possible de demander à Python de vérifier plusieurs conditions les une à la suite des autres
# en utilisant les instructions if, elif, else

# Dès que la première condition évaluée à True est trouvée, Python sort du bloc

age = 18
inscritIDEE = True
if age >= 18 and inscritIDEE:
    print("Cette ligne s'exécute parce que l'age est bien supérieur ou égal à 18 et inscrit en IDEE")
elif age <= 18 and inscritIDEE:
    ("Cette ligne s'exécute parce que l'age est inférieur ou égal à 18 et et inscrit en IDEE")
elif age <= 18 and inscritIDEE:
    ("Cette ligne s'exécute parce que l'age est inférieur ou égal à 18 et et inscrit en IDEE")
else:
    print("Ce code est exécuté parce que toutes les conditions précédentes ont échoué.")

print("Le code qui s'exécute quand Python sort du bloc if")

# L'opérateur % s'appelle le modulo