import json

def saveJSON(title, data):
    with open(title, "w", encoding='utf-8') as outfile:  
        json.dump(data, outfile, ensure_ascii=False, indent=2) 