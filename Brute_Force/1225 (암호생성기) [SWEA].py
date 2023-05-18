# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AV14uWl6AF0CFAYD&categoryId=AV14uWl6AF0CFAYD&categoryType=CODE&problemTitle=&orderBy=RECOMMEND_COUNT&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=2
# 1225. [S/W 문제해결 기본] 7일차 - 암호생성기 [D3] -> 📊 스택
# 
# 
# 
# 
# --------------------------------------------------------------------------
import sys
input = sys.stdin.readline

TC = 10

for tc in range(1,TC+1):
    test_case = int(input())
    arr = list(map(int,input().split()))
    i = 1
    while True:
        if i > 5: # 사이클은 5까지 이므로 다시 리셋
            i = 1
        temp = arr.pop(0)
        temp -= i
        if temp <= 0: # 음수 혹은 0이 발생되면 멈춰라
            temp = 0
            arr.append(temp)
            break
        else:
            arr.append(temp)
        i+=1
    # 출력
    print('#{} {}'.format(tc,' '.join(map(str,arr))))
# --------------------------------------------------------------------------
