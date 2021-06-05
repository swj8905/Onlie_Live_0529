from selenium import webdriver
import chromedriver_autoinstaller
import time

chrome_path = chromedriver_autoinstaller.install()
browser = webdriver.Chrome(chrome_path)  # 크롬 브라우저가 열림.

# 로그인 페이지로 이동
browser.get("https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com")
# 아이디 입력
id = browser.find_element_by_css_selector("input#id")
id.send_keys("talingpython")
# 비밀번호 입력
pw = browser.find_element_by_css_selector("input#pw")
pw.send_keys("q1w2e3!@#")
# 로그인 버튼 클릭하기
button = browser.find_element_by_css_selector("input.btn_global")
button.click()

