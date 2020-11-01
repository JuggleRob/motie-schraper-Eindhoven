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


def create_motie_dictionary(url):
    start_page = requests.get(url)
    start_soup = bs(start_page.content, features='html.parser')
    table = start_soup.find('table')

    for row in table.find_all('tr'):
        cells = row.find_all('td')
        if len(cells) == 9:
            bron = get_bron_pdf(base_url + cells[0].a['href'])
            titel = cells[0].a['title']
            datum = cells[2].text
            indieners = cells[6].text.replace(' ', '').split(',') # Enkel partij, nog niet de personen
            uitslag = cells[7].text 
            stemmen_voor = []
            stemmen_tegen = []
            if uitslag == "Verworpen" or uitslag == "Aangenomen":
                stemgedrag = scrape_votes(bron, titel)
                stemmen_voor = stemgedrag[0]
                stemmen_tegen = stemgedrag[1]
            motie_info = {}
            motie_info['bron'] = bron
            motie_info['titel'] = titel
            motie_info['datum'] = datum
            motie_info['indieners'] = indieners
            motie_info['uitslag'] = uitslag
            motie_info['stemmen voor'] = stemmen_voor
            motie_info['stemmen tegen'] = stemmen_tegen
            moties.append(motie_info)
            print(motie_info)
        print()