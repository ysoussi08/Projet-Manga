import requests
import urllib.request
import os
from PIL import Image
import shutil
if __name__ == '__main__':
    def dossier():
        os.chdir(r"C://Users//souss//Desktop//NSI")

    dossier()
import MangaVinland as MV
import LelScan as LS
import Scanvf as SV

path = r"C://Users//souss"

def Download(download_url,name):
    if download_url != "Fin du Manga":
        if download_url != "https://s3.mangareader.net/images/erogesopt.jpg":
            #On fait une requête et on cache le fait que l'on est un robot
            req = urllib.request.Request(download_url, headers={'User-Agent': 'Mozilla/5.0'})

            #on prend le content de la page en bytes
            web_byte = urllib.request.urlopen(req).read()

            #on écrit le content dans un fichier test et on lui file le bon format
            open(name + '.jpg','wb').write(web_byte)
            print(download_url)


def Compression():
    os.mkdir("Compr")
    ListeNon = []
    for elt in os.listdir():
        try:
            print(elt)
            im = Image.open(elt)
            im.save("Compr/" + elt,quality = 50, optimize = True)
        except:
            try:
                shutil.copy(elt,"Compr/" + elt)
            except:
                print("Erreur pour elt")
                ListeNon.append(elt)
    return ListeNon



class Site:
    def __init__(self,url,Titre):
        self.url = url
        self.soup = ""
        self.ListeLiens = []
        self.Titre = Titre
        self.chapter = ""
        self.compteur = 0


    def Initialisation(self):
        os.chdir(path)
        if self.Titre not in os.listdir():
            os.mkdir(self.Titre)
        os.chdir(self.Titre)
        with open('Titre.txt','w+') as file:
            file.write(self.Titre)


    def Navigate(self):
        if 'MangaVinland' in self.url:
            [self.soup,self.ListeLiens] = MV.Navigate(self.url)
        if 'LelScan' in self.url:
            [self.soup,self.ListeLiens] = LS.Navigate(self.url)
        if 'Scanvf' in self.url:
            [self.soup,self.ListeLiens] = SV.Navigate(self.url)


    def Next(self):
        if 'MangaVinland'in self.url:
            self.url= MV.Next(self.soup,self.url)
        if 'LelScan' in self.url:
            self.url= LS.Next(self.soup,self.url)
        if 'Ccanvf' in self.url:
            self.url= SV.Next(self.soup,self.url)

    def DownloadListe(self):
        for lien in self.ListeLiens:
            self.compteur +=1
            Download(lien,f"{self.compteur:05d}")

    def InitSoup(self):
        while self.url != "Fin du Manga":
            self.Navigate()
            self.Initialisation()
            self.DownloadListe()
            self.Next()
            print(self.url)
    def ReprendreSoup(self):
        os.chdir(self.Titre)
        self.Navigate()
        self.Next()
        while self.url != "Fin du Manga":
            self.Navigate()
            self.DownloadListe()
            self.Next()
        os.chdir("..")



def Reprise():
    os.chdir(path)
    ListeSite = []
    for dossier in os.listdir():
        if os.path.isdir(dossier):
            os.chdir(dossier)
            with open("LastUrl.txt","r") as file:
                url = file.read()
            with open("Titre.txt","r") as file:
                Titre = file.read()
            Sitee = Site(url,Titre)
            ListeSite.append(Sitee)
            os.chdir("..")
    for site in ListeSite:
        site.ReprendreSoup()
    return ListeSite

def BoucleCompr():
    os.chdir(path)
    for dossier in os.listdir():
        if os.path.isdir(dossier):
            os.chdir(dossier)
            Compression()
            os.chdir("..")