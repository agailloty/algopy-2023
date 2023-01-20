Dim TN, TI, TR, TP
TN = 0.2
TI = 0.1
TR = 0.055
TP = 0.021
MsgBox "Bonjour, bienvenue dans ce programme"
MsgBox "Voici les taux de TVA en vigueur en France" & vbNewLine & _
		"Taux normal : " & TN & vbNewLine & _
		"Taux intermédiaire : " & TI & vbNewLine & _
		"Taux réduit : " & TR & vbNewLine & _
		"Taux particulier : " & TP
Dim TAUX_CHOISI
TAUX_CHOISI = InputBox("Veuillez taper TN pour le taux normal, TI pour le taux intermédiaire, TR pour le taux réduit et TP pour le taux particulier")

If TAUX_CHOISI <> "TN" and TAUX_CHOISI <> "TI" and TAUX_CHOISI <> "TR" and TAUX_CHOISI <> "TP" Then
	MsgBox "Veuiller saisir une valeur dans la liste suivante : TN, TI, TR, TP"
	Wscript.Quit
end if

Dim MONTANT, RESULTAT
MONTANT = InputBox("Veuillez entrer le montant en EUR")


If TAUX_CHOISI = "TN" Then
	RESULTAT = MONTANT * TN
ElseIf TAUX_CHOISI = "TI" Then
	RESULTAT = MONTANT * TI
elseif TAUX_CHOISI = "TR" Then
	RESULTAT = MONTANT * TR
elseif TAUX_CHOISI = "TP" Then
	RESULTAT = MONTANT * TP
end if


MsgBox "La TVA pour le montant saisi est de " & RESULTAT & " EUR"
