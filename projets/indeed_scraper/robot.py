"""
Ce module se charge de ne faire qu'une seule chose : ouvrir le navigateur, lire une page web et
écrire le contenu de la page dans un fichier html.
"""
from selenium import webdriver

chrome = webdriver.Chrome()
# On définit une fonction save_html qui se charge de récupérer la page HTML et 
# l'enregistre sur le disque dur de l'ordinateur. 
# Il faut lui fournir en argument un url valide et un nom de fichier au format html
def save_html(url, filename):
    chrome.get(url)
    with open(filename, "w", encoding="utf-8") as f:
        f.write(chrome.page_source)

def get_html_page(url):
    chrome.get(url)
    return chrome.page_source
