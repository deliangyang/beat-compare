import xlrd
import json
import difflib
import csv
from tqdm import tqdm
import threading
from queue import Queue

from utils import replace
from utils import replace_dot_zero

wb = xlrd.open_workbook('data/13.xls')
ws = wb.sheet_by_index(0)

with open('data/artist.json', 'r') as fr:
    target = json.load(fr)

singers = target.keys()


def compare(__song_name, __target) -> list:
    percent = 0
    __item = []
    for tg in __target:
        nex_code, old, old_jrc, song_name, sub_title, artist, lyrics, song = tg
        we_song_name, target_song_name = replace(__song_name), replace(song_name)
        if we_song_name == target_song_name:
            return [
                nex_code, replace_dot_zero(old, old_jrc), song_name, sub_title,
                artist, lyrics, song, 100.00,
            ]
        __percent = difflib.SequenceMatcher(None, we_song_name, target_song_name).quick_ratio()
        if percent < __percent:
            percent = __percent
            __item = [
                nex_code, replace_dot_zero(old, old_jrc), song_name, sub_title,
                artist, lyrics, song, '%.2f' % (__percent * 100),
            ]
    return __item


def get_items():
    for i in tqdm(range(2, ws.nrows)):
        __item = ws.row_values(i)[0:5]
        item = list(map(lambda x: str(x).strip(), __item))
        yield item


__singers = {}


def diff_singer():
    for item in get_items():
        beat, we_singer, we_song, da_j, work_code = item
        if we_singer in singers:
            __singers[we_singer] = we_singer
        if we_singer not in __singers:
            __singers[we_singer] = __diff_singer(we_singer)


def __diff_singer(we_singer):
    percent = 0
    __singer = ''
    for s in singers:
        __percent = difflib.SequenceMatcher(None, we_singer, s).quick_ratio()
        if percent < __percent:
            percent = __percent
            __singer = s
    return __singer


def diff_song():
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
        queue = Queue()
        for item in get_items():
            queue.put(item)

        lock = threading.Lock()
        threads = []
        for _ in range(10):
            td = ProcessCompare(queue, lock, spam_writer, ll)
            td.start()
            threads.append(td)

        for thread in threads:
            thread.join()


def write_compare_result(spam_writer, ll, item):
    beat, we_singer, we_song, da_j, work_code = item
    # print((beat, we_singer, we_song, da_j, work_code))
    if we_singer in __singers:
        we_singer = __singers[we_singer]
    if we_singer in target:
        res = compare(we_song, target[we_singer])
        tmp = item
        if len(res) > 0:
            tmp += res
            tmp[4] = str(tmp[6]).replace('-', '')
        spam_writer.writerow(tmp)
    else:
        spam_writer.writerow([''] * ll)


class ProcessCompare(threading.Thread):
    __slots__ = ('queue', 'lock', 'csv', 'll',)

    def __init__(self, queue: Queue, lock: threading.Lock, __csv, ll):
        threading.Thread.__init__(self)
        self.queue = queue
        self.lock = lock
        self.csv = __csv
        self.ll = ll

    def run(self) -> None:
        while not self.queue.empty():
            item = self.queue.get()
            print('thread: %s, left: %d' % (self.name, self.queue.qsize()))
            self.lock.acquire()
            write_compare_result(self.csv, self.ll, item)
            self.lock.release()


if __name__ == '__main__':
    # diff_singer()
    # with open('data/singer.json', 'w') as fw:
    #     json.dump(__singers, fw)
    with open('data/singer.json', 'r') as fr:
        __singers = json.load(fr)
    # pprint.pprint(__singers)
    diff_song()
