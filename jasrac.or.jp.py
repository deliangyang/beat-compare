from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from find_content import parse, parse_header
from xlrd import open_workbook
import traceback
import json
import csv



def read_excel(filename):
    with open(filename, newline='', encoding='utf-16') as csvfile:
        spamreader = csv.reader(csvfile, delimiter='\t', quotechar='"')
        for row in spamreader:
            yield row


def agree():
    try:
        _agree_btn = driver.find_element_by_xpath('//*[@id="main_contents"]/main/form/button')
        driver.execute_script("$(arguments[0]).click()", _agree_btn)
        # _agree_btn.click()
    except Exception as e:
        print('match agree page: ', e)


def search(beat, song, singer):
    agree()
    if driver.current_url.index('eJwid') < 0:
        driver.get('http://www2.jasrac.or.jp/eJwid/')
        agree()

    song_input = driver.find_element_by_xpath('//*[@id="searchForm"]/div[1]/dl[3]/dd/div/input')
    singer_input = driver.find_element_by_xpath('//*[@id="searchForm"]/div[1]/dl[6]/dd/div/input')

    # '万葉集', 'レキシ'
    song_input.clear()
    song_input.send_keys(song)

    singer_input.clear()
    singer_input.send_keys(singer)

    search_btn = driver.find_element_by_xpath('//*[@id="searchForm"]/div[2]/button[2]')
    driver.execute_script("$(arguments[0]).click()", search_btn)

    datum = []
    try:
        html_content = driver.find_element_by_xpath('//*[@id="main_contents"]/main/div[2]/table').get_attribute(
            "outerHTML")
        datum.extend(parse_header(html_content))
        now_handle = driver.current_window_handle  # 获取当前窗口的句柄

        if len(driver.window_handles) == 1:
            try:
                search_btn = driver.find_element_by_xpath(
                    '//*[@id="main_contents"]/main/div[2]/table/tbody/tr[2]/td[6]/a')
                print(search_btn)
                driver.execute_script("document.getElementsByClassName('AUTO_JUMP')[0].click()", search_btn)
            except Exception as e:
                print("can't auto jump: ", e)

        all_handles = driver.window_handles  # 获取到当前所有的句柄,所有的句柄存放在列表当中
        for handles in all_handles:
            if now_handle != handles:
                driver.switch_to.window(handles)
        html = driver.execute_script('return $("#tab-00-00").html();')
        print(html)
        datum.append(parse(html))

        if len(driver.window_handles) > 1:
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
    except Exception as e:
        print(e)
        traceback.print_exc()
    return datum


if __name__ == '__main__':
    chrome_option = Options()
    chrome_option.add_argument('--headless')
    chrome_option.add_argument('--disable-dev-shm-usage')
    chrome_option.add_argument('--no-sandbox')

    driver = webdriver.Chrome(
        executable_path='data/chromedriver',
        chrome_options=chrome_option)
    driver.implicitly_wait(30)

    with open('beat.txt', 'r') as fr:
        __beat = fr.read().strip()

    print(__beat)
    beat_id = 0

    try:
        count = 0
        with open('xxx.txt', 'a+') as f:
            for item in read_excel('data/第二批2万首.csv'):
                no, version, beat, song, _, _, singer = item[0:7]
                if count == 0:
                    if str(beat) != str(__beat):
                        continue
                    count += 1
                    continue

                try:
                    driver.get('http://www2.jasrac.or.jp/eJwid/')
                    res = search(beat, song, singer)
                    a = [beat]
                    a.extend(res)
                    __data = json.dumps(a)
                    print(__data)
                    f.write(__data + "\n")
                    f.flush()
                    beat_id = beat
                except Exception as e:
                    print(e)
                    pass
        driver.close()
    except Exception as e:
        print(e)
        driver.close()
    except KeyboardInterrupt as e:
        print(e)
        driver.close()
    finally:
        if beat_id:
            with open('beat.txt', 'w') as fw:
                fw.write(str(beat_id))
