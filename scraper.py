##########################
# Made by Rob van Heijst #
##########################

import json
import os
import requests
from bs4 import BeautifulSoup as bs
import pdf_downloader
import vote_scraper
import pathlib

base_url = "https://eindhoven.parlaeus.nl"
moties =  []

#### TO DO LIST ####
# -naam indiener   #
# -tekst motie     #
# -handm. datum-   #
#    instellen     #
####################

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
    results = vote_scraper.count_votes(path)
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

def save_data(title, data):
    with open(title, "w", encoding='utf-8') as outfile:  
        json.dump(data, outfile, ensure_ascii=False, indent=2) 

def main():
    # Itereert over alle moties van elke maand in elk jaar
    for year in range(2018,2022):
        for month in range(1,13):
            page_url = base_url + "/user/motie/mn=" + str(month) + "/yr=" + str(year)
            #get_pdf_links_from_page(page_url)
            try:
                create_motie_dictionary(page_url)
            except Exception as e:
                print(e)
                print("Het maandnummer " + str(month) + " in het jaar " + str(year) + " heeft geen moties.")

    save_data("moties.json", moties)
    print("Aantal moties: " + str(len(moties)))

if __name__ == "__main__":
    main()
