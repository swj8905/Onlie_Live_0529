from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import chromedriver_autoinstaller

chrome_path = chromedriver_autoinstaller.install()
browser = webdriver.Chrome(chrome_path)
browser.get("https://www.youtube.com/watch?v=gIdARWrTesU")
time.sleep(4)

# 스크롤 한번 살짝 내려서 맨처음 댓글 불러오기
elem = browser.find_element_by_css_selector("html")
elem.send_keys(Keys.PAGE_DOWN)
time.sleep(4) # 댓글 불러오는 시간 기다리게 하기

comments = browser.find_elements_by_css_selector("#content-text")
idx = 0
while True:
    try:
        print(comments[idx].text)
    except:
        print("크롤링 끝!")
        browser.close()
        break
    idx += 1
    if idx % 20 == 0:
        elem = browser.find_element_by_css_selector("html")
        elem.send_keys(Keys.END)
        time.sleep(4)  # 댓글 불러오는 시간 기다리게 하기
        comments = browser.find_elements_by_css_selector("#content-text")

