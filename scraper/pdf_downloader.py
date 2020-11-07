import requests
import pathlib

def download_pdf_file(url, path):
	try:
		pdf = requests.get(url)
		open(path, 'wb').write(pdf.content)
	except:
		print("\033[91mFailed downloading the pdf: " + url + "\033[0m")
	return