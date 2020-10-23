from selenium import webdriver
import sys
from selenium.webdriver.chrome.options import Options
import time


def agree():
    try:
        _agree_btn = driver.find_element_by_xpath('//button[@id="id2"]')
        driver.execute_script("$(arguments[0]).click()", _agree_btn)
        # _agree_btn.click()
    except Exception as e:
        print('match agree page: ', e)


def search(beat, song, singer):
    agree()
    # print(driver.find_element_by_xpath("//*").get_attribute("outerHTML"))
    song_input = driver.find_element_by_xpath('//*[@id="id4"]/div[4]/div/div/input')
    singer_input = driver.find_element_by_xpath('//*[@id="id3"]')

    # '万葉集', 'レキシ'
    song_input.clear()
    song_input.send_keys(song)

    singer_input.clear()
    singer_input.send_keys(singer)

    search_input = driver.find_element_by_xpath('//*[@id="search"]')
    # 切换为无头浏览器
    driver.execute_script("$(arguments[0]).click()", search_input)
    # search_input.click()

    html = ''
    __get = False
    if str(driver.current_url).find('result'):
        html = driver.find_element_by_xpath("//*").get_attribute("outerHTML")
        __get = True
    with open('data/result/%s.html' % beat, 'w') as fw:
        fw.write(html)

    if __get:
        driver.back()
    if not str(driver.current_url).startswith('https://search.nex-tone.co.jp/condition'):
        driver.get('https://search.nex-tone.co.jp/condition?11')
    time.sleep(.2)

# driver.close()


if __name__ == '__main__':
    index = sys.argv[1]
    with open('data/c_%s.txt' % index, 'r') as fr:
        count = int(fr.read())

    chrome_option = Options()
    # chrome_option.add_argument('--headless')
    # chrome_option.add_argument('--disable-dev-shm-usage')
    # chrome_option.add_argument('--no-sandbox')

    driver = webdriver.Chrome(
        executable_path='data/chromedriver',
        chrome_options=chrome_option)

    driver.get('https://search.nex-tone.co.jp/condition?100')
    __count = 0
    with open('data/s_%s.txt' % index, 'r') as fr:
        for line in fr.readlines():
            if __count < count:
                __count += 1
                continue
            beat, singer, song = line.strip().split('\t')
            search(beat, song, singer)
            with open('data/c_%s.txt' % index, 'w') as fw:
                fw.write(str(__count))
            print((beat, singer, song))
            __count += 1
    driver.close()
