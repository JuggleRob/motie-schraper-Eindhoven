##########################
# Made by Rob van Heijst #
##########################

from PyPDF2 import PdfFileReader
from pathlib import Path
import re
import pdf_downloader

# Positive votes are in favour, negative votes are against the motie
votes_in_favour = {
        "GL": "0",
        "PvdA": "0",
        "CDA": "0",
        "D66": "0",
        "LPF": "0",
        "50PLUS": "0",
        "LE": "0",
        "CU": "0",
        "M.A. Schreurs": "0",
        "OAE": "0",
        "DENK": "0",
        "H.A.G. de Leeuw": "0",
        "VVD": "0",
        "SP": "0"
}

votes_against = {
        "GL": "0",
        "PvdA": "0",
        "CDA": "0",
        "D66": "0",
        "LPF": "0",
        "50PLUS": "0",
        "LE": "0",
        "CU": "0",
        "M.A. Schreurs": "0",
        "OAE": "0",
        "DENK": "0",
        "H.A.G. de Leeuw": "0",
        "VVD": "0",
        "SP": "0"
}

parties = ["GL", "PvdA", "CDA", "D66", "LPF", "50PLUS", "LE", "CU", "M.A. Schreurs", "OAE", "DENK", "H.A.G. de Leeuw", "VVD", "SP"]

# Takes a political party as an input and outputs a regex string in order to find the number of votes
def get_party_regex(party):
    return r"" + party + "\s?\(([0-9]+)\)"

def reset_votes():
    for key in votes_in_favour:
        votes_in_favour[key] = '0'
        votes_against[key] = '0'

# Returns a 2D array with two elements: [[votes in favour],  [votes against]
# If the decision is unaniem it returns: [[unaniem], [unaniem]]
def count_votes(path):
    # Put all the votes to zero before counting
    reset_votes()
    # Reader can manipulate PDF files
    pdf_reader = PdfFileReader(str(path))

    # This contains the last page where all the votes should be
    vote_page = pdf_reader.getPage(pdf_reader.getNumPages() - 1).extractText().replace('\n', '')

    # with this index we can classify whether a vote is in favour or against
    # we do this by checking if the vote happened before the word "Tegen:"
    try:
        index_votes_against = vote_page.find("Tegen:")
    except Exception as e:
        print("Het automatisch stemmentellen van motie " + str(path) + " is mislukt. Doe dit handmatig.")
        print("De string Tegen: staat niet op de pdf-pagina")
        print("Er is de volgende foutmelding: " + e)
        return [["vul handmatig in"],["vul handmatig in"]]

    # these arrays will be returned with the votes
    result_in_favour= []
    result_against = []
    results = [[],[]]

    if("Unaniem" in vote_page or "unaniem" in vote_page):
        return [["unaniem"], ["unaniem"]]

    # finds all the votes from all the parties
    for party in parties:
        try:
            votes = re.search(get_party_regex(party), vote_page)
            if (index_votes_against > vote_page.find(party + " (" + votes.group(1) + ")")):
                # these parties voted in favour of the motie
                votes_in_favour[party] = votes.group(1)
            else:
                # these parties voted against the motie
                votes_against[party] = votes.group(1)
        except:
            print("De partij " + party + " zat niet in de gemeenteraad.")

    # Put all the votes in favour in the array result_in_favour
    for party in votes_in_favour:
        if votes_in_favour[party] != '0':
            result_in_favour.append(party + ":" + votes_in_favour[party])

    # Put all the votes against in the array result_against
    for party in votes_against:
        if votes_against[party] != '0':
            result_against.append(party + ":" + votes_against[party])

    if len(result_in_favour) == 0 or len(result_against) == 0:
        print("Er is iets fout gegaan met tellen bij de motie: " + str(path))
        print("Tel stemmen handmatig")
        return [["vul handmatig in"],["vul handmatig in"]]
    else:
        return [result_in_favour, result_against]