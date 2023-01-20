# coding: utf-8
# Algorithme TVA
TN = 0.2
TI = 0.1
TR = 0.055
TP = 0.021

print("Bonjour, bienvenue dans ce programme")
print("Voici les taux de TVA en vigueur en France" + "\n" + 
     "Taux normal : " + str(TN) + "\n" + 
     "Taux intermédiaire : " + str(TI) + "\n" + 
     "Taux réduit : " + str(TR) + "\n" + 
     "Taux particulier : " + str(TP))
TAUX_CHOISI = input("Veuillez taper TN pour le taux normal, TI pour le taux intermédiaire, TR pour le taux réduit et TP pour le taux particulier : ")
if (TAUX_CHOISI != "TN") & (TAUX_CHOISI != "TI") & (TAUX_CHOISI != "TR") & (TAUX_CHOISI != "TP"):
    raise Exception("Veuillez saisir une valeur dans la liste suivante : TN, TI, TR, TP")
MONTANT = input("Veuiller entrer le montant : ")
MONTANT = float(MONTANT)

if TAUX_CHOISI == "TN":
    RESULTAT = MONTANT * TN
elif TAUX_CHOISI == "TI":
    RESULTAT = MONTANT * TI
elif TAUX_CHOISI == "TR":
    RESULTAT = MONTANT * TR
elif TAUX_CHOISI == "TP":
    RESULTAT = MONTANT * TP
    
print("La TVA pour le montant saisi est de " + str(RESULTAT) + "EUR")
input()