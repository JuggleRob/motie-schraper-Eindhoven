from .outputJSON import write_to_JSON_file
from .pdf_downloader import download_pdf_file

moties = []
base_url = "https://eindhoven.parlaeus.nl"

from .site_scraper import create_motie_dictionary

def scrape(startYear, startMonth):
    # Itereert over alle moties van elke maand in elk jaar
    for year in range(startYear,2022):
        if year > startYear:
            startMonth = 1
        for month in range(startMonth,13):
            page_url = base_url + "/user/motie/mn=" + str(month) + "/yr=" + str(year)
            try:
                create_motie_dictionary(page_url)
            except Exception as e:
                print(e)
                print("Het maandnummer " + str(month) + " in het jaar " + str(year) + " heeft geen moties.")

    write_to_JSON_file("Data/moties.json", moties)
    print("Aantal moties geschraapt: " + str(len(moties)))
    return
