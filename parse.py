import json
from bs4 import BeautifulSoup as BS
import re
import datetime as dt
import requests

with open('./genes.json', 'r') as input:
    genes = json.load(input)

base_url = 'https://www.vectorbase.org/Anopheles_stephensi/Component/Gene/Compara_Alignments/alignments?align=9160;db=core;g='

ngenes = len(genes)

orths = []

last_time = dt.datetime.today().timestamp()
diffs = []
for gene in genes[1:10]:
    page = requests.get(base_url + gene)
    tds = BS(page.text, 'html.parser').findAll('td')
    for td in tds:
        if re.search('AsteI2', td.text) is not None:
            orths.append({
                'AsteS1': gene,
                'AsteI2': td.text
            })

    new_time = dt.datetime.today().timestamp()
    diffs.append(new_time - last_time)
    last_time = new_time
    if len(diffs) > 10:
        diffs = diffs[-10:]
    time_per_it = len(diffs) / sum(diffs)
    print(ngenes / time_per_it / 60 / 60)

with open('./orths.json', 'w') as output:
    json.dump(orths, output)