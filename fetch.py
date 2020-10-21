from lxml import etree
import pprint
import re
import xlrd
import csv
from utils import replace
import difflib

wb = xlrd.open_workbook('data/13.xls')
ws = wb.sheet_by_index(0)


def get_beats():
    for i in range(2, ws.nrows):
        __item = ws.row_values(i)[0:5]
        item = list(map(lambda x: str(x).strip(), __item))
        yield item


re_replace = re.compile(r'<div class="alt-table-responsive" id="id(\d+)">')


def fetch(filename: str):
    with open(filename, 'r') as fr:
        return fr.read()


def fetch_info(cont: str) -> (bool, tuple):
    cont = re_replace.sub('<div class="alt-table-responsive" id="id12121xxx">', cont)
    ele = etree.HTML(cont)
    result = []
    for tr_ele in ele.xpath('//*[@id="id12121xxx"]/table/tbody/tr'):
        code = tr_ele.xpath('td[2]/span[1]/text()')
        jar_code = tr_ele.xpath('td[2]/span[2]/text()')
        song = tr_ele.xpath('td[3]/strong/a/span/text()')
        lyrics = tr_ele.xpath('td[4]/table/tbody/tr[1]/td[2]/span/text()')
        song_singer = tr_ele.xpath('td[4]/table/tbody/tr[2]/td[2]/span/text()')
        singer = tr_ele.xpath('td[5]/span/text()')
        if len(jar_code) <= 0:
            jar_code = ['']
        result.append((
            code[0],
            str(jar_code[0]).replace('(', '').replace(')', ''),
            song[0],
            '',
            singer[0],
            lyrics[0],
            song_singer[0],
        ))
    return result


if __name__ == '__main__':
    data = []
    with open('data/test.csv', 'w', newline='') as csv_file:
        spam_writer = csv.writer(csv_file, delimiter='\t',
                                 quotechar='|', quoting=csv.QUOTE_MINIMAL)
        __header = [
            '伴奏ID', '后台歌手', '后台歌名', '大J歌名', 'JASRAC work code',
            'NexTone编码（上方）', 'J编码（下方）', '歌曲名',
            '副标题', '歌手', '作词', '作曲', '匹配百分比 %',
        ]
        ll = len(__header)
        spam_writer.writerow(__header)
        for i in get_beats():
            beat, singer, song, da_j, jar_code = i
            try:
                content = fetch('data/result/%s.html' % beat)
                items = fetch_info(content)
                if len(items):
                    percent = difflib.SequenceMatcher(None, replace(song), replace(items[0][2])).quick_ratio()
                    # for item in items:
                    spam_writer.writerow(i + list(items[0]) + ['%.2f' % (percent * 100), ])
                else:
                    spam_writer.writerow(i)
            except Exception as e:
                # print(e)
                spam_writer.writerow(i)
                pass
                # print(e)
