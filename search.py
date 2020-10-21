import requests
import re

re_action = re.compile(r'action="([^"]+)"')

__headers = {}

__headers_str = """
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9,en;q=0.8
Cache-Control: max-age=0
Connection: keep-alive
Content-Length: 192
Content-Type: application/x-www-form-urlencoded
Cookie: _ga=GA1.3.116275940.1602836894; _gid=GA1.3.633539823.1603181310; JSESSIONID=E33D1BB69330D34C9B55614E112ED0B0
Host: search.nex-tone.co.jp
Origin: https://search.nex-tone.co.jp
Referer: https://search.nex-tone.co.jp/condition?5
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: same-origin
Sec-Fetch-User: ?1
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.80 Safari/537.36
"""


def __parse_headers():
    if len(__headers) > 0:
        return __headers
    lines = __headers_str.strip().split('\n')
    for line in lines:
        k, v = line.split(': ')
        __headers[k] = v


def search(song, singer):
    url = 'https://search.nex-tone.co.jp/condition?5-1.IFormSubmitListener-form'
    data = {
        'ida_hf_0': '',
        'freeWord': '',
        'pieceCd': '',
        'p::title': song,
        'excludeSubtitle': 'include',
        'titleMc': 'partial',
        'artist': singer,
        'artistMc': 'partial',
        'author': '',
        'authorMc': 'partial',
        'rightHolder': '',
        'rightHolderMc': 'partial',
        'sort': '1',
        'ascDesc': '1',
        'search': '',
    }
    req = requests.post(url, data=data, headers=__headers, allow_redirects=True)
    return req.text


def agree(url: str):
    if url.startswith('./'):
        url = 'https://search.nex-tone.co.jp' + url.replace('.', '')
    __res = requests.post(url, data={'id3_hf_0': '', 'accept': ''}, headers=__headers)
    return __res.text


if __name__ == '__main__':
    __parse_headers()
    res = search('万葉集', 'レキシ')
    print(res)

    # if res.find('NexTone 作品検索データベース 利用規約'):
    #     match = re_action.findall(res)
    #     if match and str(match[0]).index('terms'):
    #         print(match)
    #         print(agree(match[0]))
    # res = search('', '',)
    # print(res)
