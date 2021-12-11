# bibliotecas
import requests
from bs4 import BeautifulSoup
# Entra no site do G1 economia
class Scraper:
    def __init__(self):
        self.markup = requests.get("https://g1.globo.com/economia/").text
        self.salva_titulos = []
    def parse(self):
        soup = BeautifulSoup(self.markup, "html.parser")
        # titulos estao na tag a e tem como class> feed-post-link
        titulos = soup.find_all("a", class_ = "feed-post-link")
        for title in titulos:
            self.salva_titulos.append(title.text)
        return self.salva_titulos

# O output diario disso eh sempre diferente
for titulos in Scraper().parse():
    print("Notícia: " + titulos)




