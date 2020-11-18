# Het doel van dit programma
Dit project verzamelt/schraapt alle moties van de gemeente Eindhoven en maakt er een overzichtelijk CSV-bestand van. Dit CSV-bestand kan geopend worden in Excel.
___
## Hoe gebruik je dit programma:
In de terminal/command prompt voer je het volgende commando in:
```
python3 run.py
```
Dit programma schraapt alle informatie van de website van de gemeente Eindhoven en slaat het op als een CSV-bestand.
___
## Wat doet site_scraper.py ?
De module `scraper.py` schraapt alle informatie uit een tabel die te vinden is op de [website van gemeente Eindhoven](https://eindhoven.parlaeus.nl/user/motie). Dit doet die voor elk maand uit elk jaar. Omdat niet alle benodigde informatie te vinden is, moeten we ook informatie schrapen uit pdf bestanden. Dit doet de module pdf_scraper.py.
___
## Wat doet pdf_scraper.py ? 
De module `pdf_scraper.py` schraapt de stemresultaten uit het pdf-bestand van een motie en geeft deze terug aan het programma site_scraper.py.

## Wat doet pdf_downloader.py ? 
De module `pdf_downloader.py` download pdf-bestanden van het internet.
___
## To do list
- De tekst inhoud van de moties wordt niet geschraapt omdat dit te onregelmatig is in de pdf-bestanden.
- De namen van de indieners van de motie worden niet geschraapt
- Door onregelmatigheden in de PDF-bestand, lukt het pdf_scraper.py niet altijd de stemmen te tellen. Indien dit gebeurd, geeft het programma aan dat het handmatig genoteerd moet worden.
