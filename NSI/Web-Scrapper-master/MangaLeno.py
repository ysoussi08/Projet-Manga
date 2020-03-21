import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import os
if __name__ == '__main__':
    def dossier():
        os.chdir("Google Drive//Python//Web-Scrapper")

    dossier()

"""

Initialisation

"""


path = r"C:\Users\Utilisateur\Desktop\Manga Scrapper"
CompteurParcours = 0

Titre = "GOHS"
url = "http://manganelo.fun/the-god-of-high-school-chapter-0#1"

def Initialisation(Titre):
    os.chdir(path)
    if Titre not in os.listdir():
        os.mkdir(Titre)
    os.chdir(Titre)



def Navigate(url):
    if url != "Fin du Manga":
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        ListeLiens = RecupListeLiens(soup)
    return [soup, ListeLiens]

def RecupListeLiens(soup):
    Div = soup.findAll('div')
    L = []
    for item in Div:
        if ClasseDownload(item):
            L.append(item)
    M = L[0]
    ListeTag = M.findAll('img')
    ListeLiens = []
    for item in ListeTag:
        ListeLiens.append(item['src'])
    return ListeLiens



def Next(soup):
    NextUrl = ""
    A = soup.findAll('a')
    L = []
    for a in A:
        if a.text == "NEXT CHAPTER":
            NextUrl = a['href']
    if NextUrl == "":
        NextUrl = "Fin du Manga"
    print(NextUrl)
    return NextUrl


def ClasseDownload(item):
    bool = False
    bool = 'class' in item.attrs and (item['class'] == ['container-chapter-reader'] or item['class'] == ['vung-doc'] or item['class'] == ['comic_wraCon', 'text-center'])
    return bool

def ClasseNextDiv(item):
    bool = False
    bool = 'class' in item.attrs and (item['class'] == ['navi-change-chapter-btn'] or item['class'] == ['btn-navigation-chap'])
    return bool

def ClasseNextListe(tag):
    bool = False
    bool = 'class' in tag.attrs  and (tag['class'] ==['navi-change-chapter-btn-next','a-h'] or tag['class'] == ['next'])
    return bool

