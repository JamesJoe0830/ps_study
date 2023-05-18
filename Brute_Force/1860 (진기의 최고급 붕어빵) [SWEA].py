# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AV5LsaaqDzYDFAXc&categoryId=AV5LsaaqDzYDFAXc&categoryType=CODE&problemTitle=&orderBy=RECOMMEND_COUNT&selectCodeLang=ALL&select-1=3&pageSize=10&pageIndex=2
# 1860. 진기의 최고급 붕어빵 [D3] -> 🔥 오답 필요
#
# <문제 접근 방법>
# 0. 어떻게 그 시점마다 붕어빵이 있는지 체크할 것인가 ?
#
# ------------------------------------------------------------------------------
import sys
input = sys.stdin.readline

TC = int(input())
for test_case in range(TC):
    N, M, K = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()

    result = "Possible"

    for i in range(N):
        make = (arr[i]//M)*K - (i+1) # 🔥 오답시 봐야할 포인트
        if make < 0:
            result = "Impossible"
            break
    print('#{} {}'.format(test_case+1, result))

# ------------------------------------------------------------------------------
