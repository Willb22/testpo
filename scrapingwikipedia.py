from bs4 import BeautifulSoup
import requests

response = requests.get('https://en.wikipedia.org/wiki/List_of_best-selling_fiction_authors')
if response.ok:
    soup = BeautifulSoup(response.text, "html.parser")
    table = soup.find("table", {"class" : "wikitable"})
    tbody = table.find("tbody")
    trs = tbody.findAll("tr")
    for tr in trs:
        tds = tr.findAll("td")
        if len(tds) > 0:
            print(tds[0].find("a").text)
            print(tds[4].text)




if response.ok:
    s = BeautifulSoup(response.text, "html.parser")
    table = s.find("table", {"class": "wikitable sortable"})
    tbody = table.find("tbody")
    table_rows = tbody.findAll("tr")
    for row in table_rows:
        author = {}
        #print(row.findAll("tr"))
        liste_column = row.findAll("td")
        if len(liste_column)>0:
            author["name"] = liste_column[0].find("a").text
            #author["name"] = liste_column[0].find("a").text.replace('\n', '')
            author["speciality"] = liste_column[4].text.replace('\n', '')
            print(author)
