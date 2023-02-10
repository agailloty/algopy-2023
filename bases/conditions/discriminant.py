# Demander à l'utilisateur d'entrer la valeur de a
# Demander à l'utilisateur d'entrer la valeur de b
# Demander à l'utilisateur d'entrer la valeur de c


a = float(input("Entrer la valeur de a: ")) # La fonction input retourne une chaine de caractère
# On utilise la fonction float pour convertir cette chaine de caractère en nombre réel si possible
# si possible. Si la valeur qu'on entre n'est pas convertible en nombre réel il y a une erreur d'exécution.
b = float(input("Entrer la valeur de b: "))
c = float(input("Entrer la valeur de c: "))

delta = b**2 - 4*(a*c)
print(f"b**2 = {b**2} - 4*a*c = {4*(a*c)} {delta}")
print(f"La valeur de delta est : {delta}")

print("La racine carré d'un nombre est égal au nombre puissance 1/2")
print(f"Exemple 25**0.5 = {25**0.5} ou 36**0.5 = {36**0.5} ")

if delta > 0:
    print("Delta est positif ! ")
    # Si delta > 0 : 
    # calculer x1 = (-b - sqrt(delta) ) / 2 * a
    # calculer x2 = (-b + sqrt(delta) ) / 2 * a
    racine_delta = delta ** 0.5
    x1 = (-b - racine_delta) / 2 * a
    x2 = (-b + racine_delta) / 2 * a
    print(f"L'équation admet deux solutions x1 = {x1} et x2 = {x2} ")
    print(f"L'équation initiale {a}x**2 {+1 *b} x {+1 *c} peut être factorisé comme suit:")
    print(f"{a} (x-{x1})(x+{x2}")
elif delta == 0:
    # Calculer x = -b / 2*a
    print("Delta est égal à 0")
    x = -b / 2*a
    print(f"L'équation n'admet qu'une seule solution x1=x2 = {x}")
    print(f"L'équation initiale {a}x**2 {+1 *b} x {+1 *c} peut être factorisé comme suit:")
    print(f"{a} (x{x})**2")
else:
    print("Delta est négatif")
    print("L'équation n'admet aucune solution dans |R")



