import json
from bs4 import BeautifulSoup as BS
import re
import requests

with open('./data/genes.json', 'r') as input:
    genes = json.load(input)

base_url = 'https://www.vectorbase.org/Anopheles_stephensi/Component/Gene/Compara_Alignments/alignments?align=9160;db=core;g='

orths = []

for gene in genes[1:10]:
    page = requests.get(base_url + gene)
    tds = BS(page.text, 'html.parser').findAll('td')
    for td in tds:
        if re.search('AsteI2', td.text) is not None:
            orths.append({
                'AsteS1': gene,
                'AsteI2': td.text
            })


with open('./data/orths.json', 'w') as output:
    json.dump(orths, output)