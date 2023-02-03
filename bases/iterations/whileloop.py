# Des fois je ne sais pas avance combien de fois je veux Python exécute un bloc de code
# J'aimerais lui dire d'exécuter le combien tant qu'une condition n'est pas satisfaite. 

reponse = input("Bonjour!")

nb_times = 0
while reponse != "bonjour":
    reponse = input("Un peu de politesse cher ami. ")
    nb_times = nb_times + 1

print("Bah voilà ! C'était pas la mer à boire de dire bonjour !")
print(f"Il t 'a quand même fallu {nb_times} de tentatives pour me dire bonjour. Huum ")