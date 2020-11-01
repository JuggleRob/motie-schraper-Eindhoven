import json

def write_to_JSON_file(title, nieuweMoties):
    with open(title) as f:
        oudeMoties = json.load(f)
    with open(title, "w", encoding='utf-8') as outfile:  
        json.dump(oudeMoties + nieuweMoties, outfile, ensure_ascii=False, indent=2) 