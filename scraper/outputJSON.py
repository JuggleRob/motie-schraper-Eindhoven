import json

def write_to_JSON_file(title, nieuweMoties):
    with open(title) as f:
        oudeMoties = json.load(f)
    with open(title, "w", encoding='utf-8') as outfile:  
        json.dump(remove_duplicates(oudeMoties + nieuweMoties), outfile, ensure_ascii=False, indent=2) 

def remove_duplicates(motie_list):
    return [i for n, i in enumerate(motie_list) if i not in motie_list[n + 1:]]