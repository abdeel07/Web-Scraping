import requests
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest


HEADERS = ({'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
            AppleWebKit/537.36 (KHTML, like Gecko) \
            Chrome/90.0.4430.212 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'})

def getAllPages():
    urls = []
    nbPage = 1
    
    for i in range(104):
        i = f"https://www.barreaudenice.com/annuaire/avocats/?fwp_paged={nbPage}"
        nbPage += 1
        urls.append(i)
    return urls

def parser():
    pages = getAllPages()
    for p in pages:
        r = requests.get(p, headers=HEADERS)
        soup = BeautifulSoup(r.content, "lxml")
        avocats = soup.find_all('div', class_ = 'callout secondary annuaire-single')
        
        for avocat in avocats:
            nom = avocat.find('h3', class_ = 'nom-prenom').text.strip()
            path = r"./data.txt"
            
            with open(path, "a") as f:
                f.write(f"{nom}\n")
    
    
parser()
