# Tool to automatically gather PDFs from LaGuS MV
# Author: Simon
# Edited: 03.04.2021

from bs4 import BeautifulSoup
import requests
import re
import wget
from time import sleep
from pathlib import Path
import os
from zipfile import ZipFile


# Careful: function will delete all files in PDF-folder!
def scrapePDF():
    # URL
    url = "https://www.lagus.mv-regierung.de/Gesundheit/InfektionsschutzPraevention/Daten-Corona-Pandemie/"

    requestedText = requests.get(url)
    # Parsing HTML
    html = BeautifulSoup(requestedText.text, 'html.parser')

    downloadURL = html.find_all('div', class_="teaser_text")

    links = []
    downloadURLZIP = downloadURL
    for div in downloadURL:
        if len(div.find_all('h5', string=re.compile("MV-Lagebericht Cor"))) != 0:
            links.append(div)
    downloadURL = []
    for link in links:
        downloadURL.append(link.find('a'))

    links = []
    for tag in downloadURL:
        links.append("https://www.lagus.mv-regierung.de" + str(tag.get('href')))

    path = str(Path('.').absolute()) + "/pdf"
    # Will remove every File in PDF before downloading the new ones
    for file in os.listdir(path):
        os.remove(path + "/" + str(file))
    # Downloads files
    for link in links:
        wget.download(link, out=path)
        sleep(1)  # Sleep is required according to Robots.txt

    # Gathering ZIP-Files
    links = []
    for div in downloadURLZIP:
        if len(div.find_all('h5', string=re.compile("MV-Lageberichte Coronavirus 2021"))) != 0:
            links.append(div)
    downloadURLZIP = []
    for link in links:
        downloadURLZIP.append(link.find('a'))
    links = []
    for tag in downloadURLZIP:
        links.append("https://www.lagus.mv-regierung.de" + str(tag.get('href')))

    for link in links:
        wget.download(link, out=path)
        sleep(1)  # Sleep is required according to Robots.txt

    for zip_file in (list(Path('.').glob('pdf/*.zip'))):
        with ZipFile(zip_file) as z:
            z.extractall("pdf")
        os.remove(zip_file)


if __name__ == "__main__":
    scrapePDF()
