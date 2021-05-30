from bs4 import BeautifulSoup
import urllib.request as req

# 서버로부터 HTML 코드 받기
code = req.urlopen("http://www.cgv.co.kr/movies/")
# print(code.read())

# HTML 코드 이쁘게 정리하기
soup = BeautifulSoup(code, "html.parser")
# print(soup)

# 내가 원하는 요소 알려주기
# title = soup.select_one("strong.title")
title = soup.select("div.sect-movie-chart strong.title")
# print(title)
for i in title:
    print(i.string) # 요소 내용 출력하기