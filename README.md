# Het doel van dit programma
Dit project verzamelt/schraapt alle moties van de gemeente Eindhoven en maakt er een overzichtelijk JSON-bestand van.

# Hoe gebruik je dit programma:
In de terminal/command prompt voer je het volgende commando in:

python3 scraper.py

Dit laat het programma scraper.py beginnen met werken. Het programma scraper.py roept automatisch alle andere programma's aan die nodig zijn. Als het programma klaar is, heb je eens JSON-bestand waar alle moties in staan.

# Wat doet scraper.py ?
Het programma scraper.py verzamelt/schraapt alle informatie uit een tabel die te vinden is op de website https://eindhoven.parlaeus.nl/user/motie . Dit doet die voor elk maand uit elk jaar. Omdat niet alle benodigde informatie te vinden is in deze tabel, zijn er andere programma's nodig om deze informatie te verzamelen.

# Wat doet pdf_downloader.py ? 
Het programma pdf_downloader.py download pdf-bestanden van het internet.

# Wat doet vote_scraper.py ? 
Het programma vote_scraper.py schraapt de stemresultaten uit het pdf-bestand van een motie en geeft deze terug aan het programma scraper.py.

# TO DO LIST
- Momenteel worden telkens alle moties geschraapt. Je zou de begindatum moeten kunnen instellen.
- De tekst inhoud van de moties wordt niet geschraapt omdat dit te onregelmatig is in de pdf-bestanden.
- De namen van de indieners van de motie worden niet geschraapt
- Het CSV-bestand en het excel-bestand worden niet automatisch gemaakt.
