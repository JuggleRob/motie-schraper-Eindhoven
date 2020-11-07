# Het doel van dit programma
Dit project verzamelt/schraapt alle moties van de gemeente Eindhoven en maakt er een overzichtelijk CSV-bestand van. Dit CSV-bestand kan geopend worden in Excel.

# Hoe gebruik je dit programma:
In de terminal/command prompt voer je het volgende commando in:

python3 run.py

Dit programma schraapt alle informatie van de website van gemeente Eindhoven en slaat het op als een JSON-bestand in de folder Data.

# Wat doet site_scraper.py ?
De module scraper.py schraapt alle informatie uit een tabel die te vinden is op de website https://eindhoven.parlaeus.nl/user/motie . Dit doet die voor elk maand uit elk jaar. Omdat niet alle benodigde informatie te vinden is in deze tabel, zijn er andere programma's nodig om deze informatie te verzamelen.

# Wat doet pdf_scraper.py ? 
De module pdf_scraper.py schraapt de stemresultaten uit het pdf-bestand van een motie en geeft deze terug aan het programma site_scraper.py.

# Wat doet pdf_downloader.py ? 
De module pdf_downloader.py download pdf-bestanden van het internet.

# TO DO LIST
- De tekst inhoud van de moties wordt niet geschraapt omdat dit te onregelmatig is in de pdf-bestanden.
- De namen van de indieners van de motie worden niet geschraapt
- Door onregelmatigheden in de PDF-bestand, lukt het pdf_scraper.py niet altijd de stemmen te tellen. Indien dit gebeurd, geeft het programma aan dat het handmatig genoteerd moet worden.
