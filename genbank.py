import time

from Bio import Entrez
import json

Entrez.email = 'khanl2@mymail.vcu.edu'

f = open('./genids.json')
ids = json.load(f)[0]
id_list = []
for i in ids['protein']:
    id_list.append(i)
f.close()


def clean_seq(sq):
    sq[0] = sq[0][14:]
    return ''.join(sq[:-1])


def clean_organism(org):
    return org[11:-1]


def scrap_entrez(id):
    handle = Entrez.efetch(db='nucleotide', id=id, rettype='gb', retmode="text")
    data = handle.readline().strip()
    tran = False
    organism = ''
    translated_seq = []
    while data != '':
        if 'organism=' in data:
            if 'New York' and '/2003(' in data:
                organism = clean_organism(data)
            else:
                handle.close()
                return
        if 'translation' in data:
            tran = True
        if 'peptide' in data:
            tran = False
        if tran:
            translated_seq.append(data)
        data = handle.readline().strip()
    handle.close()
    return [organism, clean_seq(translated_seq)]


record_count = 0
for genid in id_list:
    record_count += 1
    if (record_count % 100) == 0:
        time.sleep(30)
    record = scrap_entrez(genid)
    if record != None:
        with open('newyork_records_2003.txt', 'a') as writer:
            writer.write(record[0])
            writer.write('\n')
            writer.write(record[1])
            writer.write('\n\n')
