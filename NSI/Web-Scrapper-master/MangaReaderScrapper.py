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
Titre = "Manga"



"""

Navigation dans la page Web

"""

trunk = "https://www.mangareader.net"


url = trunk + "/tate-no-yuusha-no-nariagari/1/2"




"""

Recherche de l'image dans la page web

"""

def Navigate(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    if soup.text.find("is not released") <0:
        Im = soup.findAll('img')[0]
        link = Im['src']
        download_url = [link]
    else:
        print("Fin du manga")
        download_url = "Fin du Manga"
    return [soup, download_url]



def Next(soup):
    NextUrl = ""
    Div = soup.findAll("div")
    for item in Div:
        if 'id' in item.attrs and item['id'] == 'imgholder':
            NextUrl = trunk + item.a['href']
    if NextUrl == "":
        NextUrl = "Fin du Manga"
    print(NextUrl)
    return NextUrl







