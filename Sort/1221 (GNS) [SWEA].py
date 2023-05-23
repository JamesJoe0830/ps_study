# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AV14jJh6ACYCFAYD&categoryId=AV14jJh6ACYCFAYD&categoryType=CODE&problemTitle=&orderBy=RECOMMEND_COUNT&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=4
# 1221. [S/W 문제해결 기본] 5일차 - GNS -> 🧾 정렬
# 
# <문제 접근 방법>
# many 리스트에 arr[i]별로 개수 파악하고 넣어주기 
# 
# -----------------------------------------------------------------------------
import sys
input = sys.stdin.readline

TC = int(input())

for tc in range(TC):
    idx, length = map(str,input().split())
    Nums = list(map(str,input().split()))
    arr = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    many = []
    for i in range(10):
        cnt = 0
        for j in range(int(length)):
            if Nums[j] == arr[i]:
                cnt+=1
        many.append(cnt)

    print(idx)
    for i in range(len(arr)):
        for j in range(many[i]):
            print(arr[i], end=' ')
    print()
# -----------------------------------------------------------------------------