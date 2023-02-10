from robot import save_html, get_html_page
from lxml import html

lien = "https://fr.indeed.com/jobs?q=data+analyst&l=France&from=searchOnHP&vjk=f400f062f379bb7b"
save_html(lien, "pageIndeed.html")

html_doc = html.fromstring(get_html_page(lien))
print(html_doc.xpath("//span[starts-with(@id, 'jobTitle')]/text()"))
