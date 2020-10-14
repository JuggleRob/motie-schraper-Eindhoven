##########################
# Made by Rob van Heijst #
##########################

import requests
import pathlib

def download_pdf_file(url, path):
	try:
		pdf = requests.get(url)
		open(path, 'wb').write(pdf.content)
	except:
		print("Failed downloading the pdf: " + url)
	return