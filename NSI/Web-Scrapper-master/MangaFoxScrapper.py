import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import os

if __name__ == '__main__':
    def dossier():
        os.chdir("Google Drive//Python//Web-Scrapper")

    dossier()



#Ne marche que sur MangaReader


"""

Initialisation

"""

path = r"C:\Users\Utilisateur\Desktop\Manga Scrapper"
CompteurParcours = 0
Titre = "Manga2"
url = "https://ww3.mangafox.online/the-top-clan-leader-in-history/chapter-74-1192366631948209"

"""

Navigation dans la page Web

"""


url = "https://ww3.mangafox.online/favorite-part/chapter-1-324246019529673"




"""

Recherche de l'image dans la page web

"""

def Navigate(url):
    if url != "Fin du Manga":
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        ListeLiens = RecupListeLiens(soup)
    return [soup, ListeLiens]

def RecupListeLiens(soup):
    Img = soup.findAll('img')
    ListeLiens = []
    for item in Img:
        if 'class' in item.attrs and item['class'] == ['load_img']:
            ListeLiens.append(item['src'])
    return ListeLiens







"""

Manga Fox : Suivant .find(class="next_prev") puis enfant btn"

Boucle sur les scr de class="list_img"

"""

def Next(soup):
    trunk = "https://ww3.mangafox.online"
    NextUrl = ""
    A = soup.findAll('a')
    L = []
    for a in A:
        if a.text == "Next":
            NextUrl = a['href']
    if NextUrl == "":
        NextUrl = "Fin du Manga"
    print(NextUrl)
    return NextUrl



