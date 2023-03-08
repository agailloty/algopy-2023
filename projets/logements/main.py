from selenium import webdriver
import os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(os.path.join(dname, "output"))

chrome = webdriver.Chrome()

lien = "https://www.leboncoin.fr/recherche?text=appartement&locations=Rennes__48.10980730273463_-1.6674540604783095_7662_10000"
chrome.get(lien)

with open("webpage.html", "w", encoding="utf-8") as f:
    f.write(chrome.page_source)
