import os
import requests
from bs4 import BeautifulSoup as bs
from scraper import pdf_downloader, pdf_scraper, base_url, moties
import pathlib

# Om de link naar het PDF-bestand te krijgen heb je twee links nodig
# De eerste link verwijst je naar een algemene info pagina zoals eindhoven.parlaeus.nl/user/motie/action=view/id=357.
# Op deze algemene info pagina staat een link naar het PDF-bestand
def get_bron_pdf(url):
    info_page = requests.get(url)
    soup = bs(info_page.content, features='html.parser')
    motie = soup.select_one('p a')
    url_bron = base_url + motie['href']
    return url_bron

def scrape_votes(url, title):
    path = pathlib.Path(__file__).parent.absolute().joinpath(title + ".pdf")
    pdf_downloader.download_pdf_file(url, path)
    results = pdf_scraper.count_votes(path)
    os.remove(path)
    return results

def extract(url):
    headers = { 'user-agent' : 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:82.0) Gecko/20100101 Firefox/82.0'}
    site_gemeente = requests.get(url, headers)
    soup = bs(site_gemeente.content, 'html.parser')
    return soup

def create_motie_dictionary(url):
    soup = extract(url)
    table = soup.find('table')
    tablerows = table.find_all('tr')

    for row in tablerows:
    
        cells = row.find_all('td')
        if len(cells) == 9:
            bron = get_bron_pdf(base_url + cells[0].a['href'])
            titel = cells[0].a['title']
            datum = cells[2].text
            indieners = cells[6].text.replace(' ', '').split(',') # Enkel partij, nog niet de personen
            uitslag = cells[7].text 
            voor = []
            tegen = []
            unaniem = "nee"
            if uitslag == "Verworpen" or uitslag == "Aangenomen":
                stemgedrag = scrape_votes(bron, titel)
                voor = stemgedrag[0]
                tegen = stemgedrag[1]
                if voor[0] == 'unaniem':
                    unaniem = "ja"
                    voor = []
                    tegen = []
            motie_info = {
                'bron' : bron,
                'titel' : titel,
                'datum' : datum,
                'indieners' : indieners,
                'uitslag' : uitslag,
                'voor' : voor,
                'tegen' : tegen,
                'unaniem' : unaniem
            }
            moties.append(motie_info)
            print(f'\033[92m Motie geschraapt: {titel} \033[0m')