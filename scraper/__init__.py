from .pdf_downloader import download_pdf_file
import pandas as pd
from datetime import datetime

moties = []
base_url = "https://eindhoven.parlaeus.nl"

from .site_scraper import create_motie_dictionary

def scrape(startYear, startMonth):
    # Itereert over alle moties van elke maand in elk jaar
    currentYear = datetime.now().year
    lastMonth = 13
    for year in range(startYear, currentYear + 1):
        if year > startYear:
            startMonth = 1
        if year == currentYear:
            lastMonth = datetime.now().month

        for month in range(startMonth,lastMonth + 1):
            page_url = base_url + "/user/motie/mn=" + str(month) + "/yr=" + str(year)
            try:
                create_motie_dictionary(page_url)
            except Exception as e:
                print("\033[91m" + str(e) + "\033[0m")
                print("Het maandnummer " + str(month) + " in het jaar " + str(year) + " heeft geen moties.")

    dataframe = pd.DataFrame(moties)
    with open('moties.csv', 'a') as f:
        dataframe.to_csv(f, header=f.tell()==0)
    df = pd.read_csv('moties.csv')
    df.drop_duplicates(subset=['titel'], inplace=True)
    df.to_csv('moties.csv', index=False)

    print('\nAlle geschraapte moties zitten nu in het bestand moties.csv')

    return
