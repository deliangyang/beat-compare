import json

data = {}
with open('xxx.txt', 'r') as fr:
    for line in fr.readlines():
        line = json.loads(line)
        if len(line) == 1:
            continue
        if len(line) == 6:
            line.extend([{}, ])
            data[line[0]] = line
        else:
            if line[0] not in data:
                data[line[0]] = line
            elif len(data[line[0]]) > len(line):
                data[line[0]] = line

data2 = {}
for _k, _v in data.items():
    beat, _, code, song, singer, singer2, extra = _v
    _tmp = {
        'lyric': '',
        'song': '',
    }
    for k, v in extra.items():
        if str(k).find('作詞') >= 0:
            _tmp['lyric'] = ', '.join(v).replace('\u3000', ' ')
        elif str(k).find('作曲') >= 0:
            _tmp['song'] = ', '.join(v).replace('\u3000', ' ')
    data2[beat] = [code, song, singer2, _tmp['lyric'], _tmp['song']]

from xlrd import open_workbook
import csv


def read_excel(filename):
    wb = open_workbook(filename)
    ws = wb.sheet_by_index(0)
    for row_index in range(ws.nrows):
        yield ws.row_values(row_index)


def read_excel_csv(filename):
    with open(filename, newline='', encoding='utf-16') as csvfile:
        spamreader = csv.reader(csvfile, delimiter='\t', quotechar='"')
        for row in spamreader:
            yield row



import openpyxl

workbook = openpyxl.Workbook()
sheet = workbook.active


for item in read_excel_csv('data/第二批2万首.csv'):
    # print(item[2])
    item[6] = str(item[6]).replace('\x1a', ' ')
    item[3] = str(item[3]).replace('\x1a', ' ')
    try:
        if item[2] in data2:
            item.extend(data2[item[2]])
        sheet.append(item)
    except Exception as e:
        print(item)

workbook.save('new.xlsx')