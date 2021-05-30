# 파일 열기 모드
# "r" 모드 : 읽기모드
# - 파일이 존재하지 않으면, 에러를 뱉음!
# - UnicodeDecodeError가 뜬다면? encoding="utf-8" 추가!
f = open("./zxcvxzvxz.txt", "r", encoding="utf-8")
result = f.readlines()
f.close()
print(result)