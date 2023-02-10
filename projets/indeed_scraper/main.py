from robot import save_html, get_html_page
from lxml import html

lien = "https://fr.indeed.com/jobs?q=data+analyst&l=France&from=searchOnHP&vjk=f400f062f379bb7b"
save_html(lien, "pageIndeed.html")

# On peut récupérer le titre de l'offre d'emploi, le nom de l'entreprise, la note, 
# la location, descriptif de l'offre d'emploi

contenu_page = get_html_page(lien)
html_doc = html.fromstring(contenu_page)


job_titles = html_doc.xpath("//span[starts-with(@id, 'jobTitle')]/text()")
company_names = html_doc.xpath("//a[@data-tn-element='companyName']/text()")
company_rankings = html_doc.xpath("//span[@class='ratingsDisplay withRatingLink']") # A prendre avec
# précaution car toutes les entreprises n'ont pas de note.
job_locations = html_doc.xpath("//span[starts-with(@id, 'jobTitle')]/text()")
job_descriptions = html_doc.xpath("//span[starts-with(@id, 'jobTitle')]/text()")
