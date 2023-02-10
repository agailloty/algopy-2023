import requests
lien = "https://fr.indeed.com/jobs?q=data+analyst&l=France&from=searchOnHP&vjk=f400f062f379bb7b"
page_indeed = requests.get(lien)

print(page_indeed.text)