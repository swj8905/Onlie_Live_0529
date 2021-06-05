from selenium import webdriver
import chromedriver_autoinstaller
import time

chrome_path = chromedriver_autoinstaller.install()
# 헤드리스 모드
opt = webdriver.ChromeOptions()
opt.add_argument("headless")
browser = webdriver.Chrome(chrome_path, options=opt)  # 크롬 브라우저가 열림.
# 헤드리스 모드가 아닌 일반 모드 쓰고 싶을 때,
# browser = webdriver.Chrome(chrome_path)  # 크롬 브라우저가 열림.

# 로그인 페이지로 이동
browser.get("https://logins.daum.net/accounts/signinform.do?url=https%3A%2F%2Fwww.daum.net%2F")
# 아이디 입력
id = browser.find_element_by_css_selector("input#id")
id.send_keys("talingpython")
# 비밀번호 입력
pw = browser.find_element_by_css_selector("input#inputPwd")
pw.send_keys("q1w2e3!@#")
# 로그인 버튼 클릭하기
button = browser.find_element_by_css_selector("button#loginBtn")
button.click()
time.sleep(3)  # 로그인할 때까지 기다리게 하기.

# 이메일함으로 이동
browser.get("https://mail.daum.net/")
time.sleep(2)  # 웹페이지 뜰 때까지 기다리게 하기.
# 이메일 제목 크롤링
title = browser.find_elements_by_css_selector("strong.tit_subject")
for i in title:
    print(i.text)  # 셀레니움에서 요소의 내용 출력할 땐 무조건 ".text"!
browser.close()  # 브라우저 창 닫아주기
