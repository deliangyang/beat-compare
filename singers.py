import xlrd

wb = xlrd.open_workbook('data/13.xls')
ws = wb.sheet_by_index(0)


def get_beats():
    for i in range(2, ws.nrows):
        __item = ws.row_values(i)[0:5]
        item = list(map(lambda x: str(x).strip(), __item))
        yield item


data = []
for i in get_beats():
    data.append('\t'.join(i[0:3]))


def split(index, __data):
    with open('data/s_%d.txt' % index, 'w') as fw:
        fw.write('\n'.join(__data))


ll = len(data)
mod = int(ll / 4)
for i in range(1, 5):
    start = (i - 1) * mod
    if i == 4:
        __data = data[(i - 1) * mod:]
    else:
        __data = data[(i - 1) * mod:i * mod]
    split(i, __data)
