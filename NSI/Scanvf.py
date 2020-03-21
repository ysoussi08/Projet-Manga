import requests
import urllib.request
import os
from PIL import Image
import shutil
from bs4 import BeautifulSoup

LeSite = "https://www.scan-vf.net/"

os.chdir("C://Users//souss//Desktop//NSI")

def Navigate(url):
    if url != "Fin du Manga":
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        ListeLiens=ListeImage(soup)
    return [soup,ListeLiens]


def ListeImage(soup):
    ListeLiens = []
    Im = soup.findAll('img')
    for elt in Im:
        if 'class' in elt.attrs and elt['class']==["img-responsive"]:
            var = elt['data-src']
            ListeLiens.append(var)
    return ListeLiens


def Next(soup,url):
    uuu=isole(url)
    bbb=Isole(url)
    NextUrl=uuu+str(bbb+1)
    a=str(NextUrl)
    if ListeImage(soup) == []:
        NextUrl = "Fin du Manga"
        print(NextUrl)
    else:
        print(NextUrl)
    return NextUrl

def Isole(url):
    bac=url.split('chapitre-')[-1]
    return int(bac)


def isole(url):
    url2 = url.split(str(isole(url)))[0]
    return url2