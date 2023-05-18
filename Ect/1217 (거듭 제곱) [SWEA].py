# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AV14dUIaAAUCFAYD&categoryId=AV14dUIaAAUCFAYD&categoryType=CODE&problemTitle=&orderBy=RECOMMEND_COUNT&selectCodeLang=ALL&select-1=3&pageSize=10&pageIndex=2
# 1217. [S/W 문제해결 기본] 4일차 - 거듭 제곱 -> 📝 수학
# 
# 
# 
# -----------------------------------------------------------------------------
import sys
input = sys.stdin.readline

TC = 10
answer = []

def Power(N,M) :
    global answer 
    power = 1

    for i in range(M):
        power *= N

    answer.append(power)



for test_case in range(TC):

    n = int(input())
    N,M = map(int, input().split())
    Power(N,M)

# 출력
for i in range(TC):
    print('#{} {}'.format(i+1, answer[i]))