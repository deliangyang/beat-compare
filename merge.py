import xlrd
import json
from openpyxl import Workbook

wb = xlrd.open_workbook('data/版权信息.xlsx')
ws = wb.sheet_by_index(0)

book = Workbook()
sheet = book.active

with open('data/a.json', 'r') as fr:
    data = json.load(fr)

if __name__ == '__main__':
    sheet.append(ws.row_values(0) + ['伴奏ID', '歌曲名', '歌手1名称', '下载量', '最近7天下载量'])
    for i in range(1, ws.nrows):
        row = ws.row_values(i)
        key = str(row[2]).strip() + str(row[1]).strip()
        if key not in data:
            sheet.append(row)
        else:
            sheet.append(row + data[key])
    book.save('data/merge.xlsx')
