from bs4 import BeautifulSoup
import urllib.request as req
import urllib.parse as par
import os

if not os.path.exists("./이미지수집"):
    os.mkdir("./이미지수집")

keyword = input("키워드 입력 >> ")

if not os.path.exists(f"./이미지수집/{keyword}"):
    os.mkdir(f"./이미지수집/{keyword}")

encoded = par.quote(keyword) # 특수한 문자로 변환
url = f"https://images.search.yahoo.com/search/images;_ylt=Awr9Il2nz7pgV2QAOm5XNyoA;_ylu=Y29sbwNncTEEcG9zAzEEdnRpZAMEc2VjA3BpdnM-?p={encoded}&fr2=piv-web&fr=yfp-t"
code = req.urlopen(url)
soup = BeautifulSoup(code, "html.parser")
img = soup.select("a > img")
cnt = 1
for i in img:
    img_url = i.attrs["data-src"]
    print(img_url) # .attrs : 요소의 속성값
    req.urlretrieve(img_url, f"./이미지수집/{keyword}/{cnt}.png") # 이미지 다운로드
    cnt += 1
