# On aurait pu utiliser la librairie requests pour les interroger les pages mais il arrive des fois
# que les serveurs bloquent les requetes. Donc on va partir avec selenium, c-a-d automatiser
# le navigateur pour lire les données. 

# On importe selenium

from selenium import webdriver
# On importe le driver web. C'est l'agent qui va utiliser le navigateur à notre place. 
# On va utiliser chrome comme navigateur

chrome = webdriver.Chrome()
lien = "https://fr.indeed.com/jobs?q=data+analyst&l=France&from=searchOnHP&vjk=f400f062f379bb7b"
chrome.get(lien)
