from biomart import BiomartServer
import json

server = BiomartServer('http://biomart.vectorbase.org/biomart')

steph = server.datasets['astephensi_eg_gene']

response = steph.search({
    'attributes': [
        'ensembl_gene_id'
    ]
})

genes = []
for line in response.iter_lines():
    line = line.decode('utf-8')
    genes.append(line)

with open('./data/genes.json', 'w') as file:
    json.dump(genes, file)