import xlrd
import json
from utils import replace

wb = xlrd.open_workbook('data/20201020175406.xlsx')
ws = wb.sheet_by_index(0)

data = {}
for i in range(1, ws.nrows):
    nex_code, old, old_jrc, song_name, sub_title, artist, lyrics, song = ws.row_values(i)[0:8]
    __artist = replace(artist)
    if __artist not in data:
        data[__artist] = []
    data[__artist].append([
        nex_code, old, old_jrc, song_name, sub_title, artist, lyrics, song
    ])

with open('data/artist.json', 'w') as fw:
    json.dump(data, fw)
