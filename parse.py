import json
import re
from bs4 import BeautifulSoup as BS
import requests
import telepot


bot = telepot.Bot(token)

with open('./data/genes.json', 'r') as input:
    genes = json.load(input)

orths = []

def get_ind_coords(gene):

    base_url = 'https://www.vectorbase.org/Anopheles_stephensi/Component/Gene/Compara_Alignments/alignments?align=9160;db=core;g='
    page = requests.get(base_url+gene, proxies={'http': '192.168.0.107:8123'})
    for td in BS(page.text, 'html.parser').findAll('td'):
        if re.search('AsteI2', td.text) is not None:
            return({
                'AsteS1': gene,
                'AsteI2': td.text
            })

for gene in genes:
    try:
        orths.append(get_ind_coords(gene))
    except BaseException as e:
        print(e)
        bot.sendMessage('78955615', text=e)
        break


with open('./data/orths.json', 'w') as output:
    json.dump(orths, output)