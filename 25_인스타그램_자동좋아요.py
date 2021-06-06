from selenium import webdriver
import time
import chromedriver_autoinstaller
import random

hash_tag = input("해시태그 입력 >> ")

chrome_path = chromedriver_autoinstaller.install()
browser = webdriver.Chrome(chrome_path)
browser.get("https://www.instagram.com/accounts/login/")
time.sleep(2)

id = browser.find_element_by_name("username")
id.send_keys("tutor_pyson") # 꼭! 본인 계정을 적어주세요.
pw = browser.find_element_by_name("password")
pw.send_keys("q1w2e3!@#") # 꼭! 본인 계정을 적어주세요.
button = browser.find_element_by_css_selector("div.Igw0E.IwRSH.eGOV_._4EzTm.bkEs3.CovQj.jKUp7.DhRcB")
button.click()
time.sleep(3)

# 해시태그 검색
url = "https://www.instagram.com/explore/tags/" + hash_tag
browser.get(url)
time.sleep(5)
# 첫번째 사진 클릭
first_photo = browser.find_element_by_css_selector("div._9AhH0")
first_photo.click()
time.sleep(3)
# 자동 좋아요 시작
while True:
    like = browser.find_element_by_css_selector("section.ltpMr.Slqrh svg._8-yf5")
    value = like.get_attribute("aria-label")
    next = browser.find_element_by_css_selector("a._65Bje.coreSpriteRightPaginationArrow")
    if value == "좋아요": # 좋아요가 안눌려있다면?
        like.click()
        time.sleep(random.randint(2, 5) + random.random())
        next.click()
        time.sleep(random.randint(2, 5) + random.random())
    elif value == "좋아요 취소": # 좋아요가 눌려있다면?
        next.click()
        time.sleep(random.randint(2, 5) + random.random())









