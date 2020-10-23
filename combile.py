import xlrd
import csv


data = {}


def read_csv_data(filename):
    with open(filename, newline='', ) as csv_file:
        spam_reader = csv.reader(csv_file, delimiter=',', quotechar='|')
        for row in spam_reader:
            beat, song, singer, download, download_in7day = row[0], row[1], row[2], row[3], row[4]
            data[song.strip() + singer.strip()] = row


read_csv_data('data/1.csv')
read_csv_data('data/2.csv')

if __name__ == '__main__':
    import json
    with open('data/a.json', 'w') as fw:
        json.dump(data, fw)
