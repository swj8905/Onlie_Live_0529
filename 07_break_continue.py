num = 0 # = : 오른쪽 값을 왼졲 변수에 저장시키는 '할당' 연산자
while True: # 무한 루프
    num += 1
    if num % 2 == 1: # 만약에 num이 홀수라면?
        continue # 반복문의 조건부로 돌려보냄.
    print(num)
    if num == 20: # == : 양 쪽의 값이 같냐?
        break # 반복문을 탈출 시킴