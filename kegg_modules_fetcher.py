"""
kegg_modules_fetcher.py

This script fetches detailed information about biological modules from the KEGG database. It takes a list of KEGG module IDs and extracts relevant data for each, including entries, symbols, names, pathway IDs, and pathway names. The script is designed to handle API rate limits by introducing a delay between requests, making it ideal for extensive bioinformatics research that requires comprehensive module information.

Written by Vikas Sharma, 2023
"""


import requests
import re
import time

def get_kegg_module_details(module_id):
    time.sleep(1)  # Wait for 1 second before making the request
    url = f"http://rest.kegg.jp/get/{module_id}"
    response = requests.get(url)
    if response.ok:
        return response.text
    else:
        return None

def get_kegg_entry_details(entry_id):
    time.sleep(1)  # Wait for 1 second before making the request
    url = f"http://rest.kegg.jp/get/{entry_id}"
    response = requests.get(url)
    if response.ok:
        return response.text
    else:
        return None

def extract_definitions(module_data):
    if module_data:
        for line in module_data.split('\n'):
            if line.startswith("DEFINITION"):
                return re.findall(r'K\d{5}', line)
    return []

def extract_symbol_and_name(entry_data):
    lines = entry_data.split('\n')
    symbol = None
    name = None
    pathways = {}

    for line in lines:
        if line.startswith("SYMBOL"):
            symbol = line.split(maxsplit=1)[-1].strip()
        if line.startswith("NAME"):
            name = line.split(maxsplit=1)[-1].strip().split(' [')[0].strip()
        if line.startswith("PATHWAY"):
            pathway_id, pathway_name = line.split(maxsplit=1)[1].strip().split('  ')
            pathways[pathway_id] = pathway_name.strip()

    pathway_ids = ';'.join(pathways.keys())
    pathway_names = ';'.join(pathways.values())

    return symbol, name, pathway_ids, pathway_names

def main():
    with open("module_ids.txt", "r") as file:
        module_ids = [line.strip() for line in file.readlines()]

    with open("module_entry_symbol_name_pathway.tsv", "w") as file:
        file.write("Module\tEntry\tSymbol\tName\tPathway ID\tPathway\n")
        for module_id in module_ids:
            module_details = get_kegg_module_details(module_id)
            if module_details:
                entries = extract_definitions(module_details)
                for entry in entries:
                    entry_details = get_kegg_entry_details(entry)
                    if entry_details:
                        symbol, name, pathway_ids, pathway_names = extract_symbol_and_name(entry_details)
                        if symbol and name: 
                            file.write(f"{module_id}\t{entry}\t{symbol}\t{name}\t{pathway_ids}\t{pathway_names}\n")

if __name__ == "__main__":
    main()
