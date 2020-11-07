##########################
# Made by Rob van Heijst #
##########################

import scraper

def main():
    year = int(input("Moties laden vanaf het jaartal (YYYY): "))
    if year < 2018:
        year = 2018
    month = int(input("Moties laden vanaf maandnummer (MM): "))
    if month < 1:
        month = 1
    print(f"\nMoties vanaf 01-{month}-{year} worden geschraapt.\n")
    scraper.scrape(year, month)

if __name__ == "__main__":
    main()
