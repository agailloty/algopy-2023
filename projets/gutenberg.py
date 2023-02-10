import requests
from lxml import html

lien = "https://www.gutenberg.org/browse/scores/top#books-last1"
page = requests.get(lien).content
#print(page) # Afficher le contenu HTML de la page

# Obtenir la liste de 100 livres les plus téléchargés ces 7 derniers jours
tree = html.fromstring(page)
books = tree.xpath("//h2[@id='books-last7']/following::a[starts-with(@href, '/ebooks')]/text()")
# Ce code ramène 200 élements mais nous ne prendrons que les 100 premiers


# Ecrire le resultat dans un fichier text nommé gutenberg.txt
with open("gutenberg.txt", "w") as f:
    for i in range(100):
        f.write(books[i] + "\n")
