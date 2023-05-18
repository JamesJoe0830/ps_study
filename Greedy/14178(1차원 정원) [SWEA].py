# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AX_N3oSqcyUDFARi&categoryId=AX_N3oSqcyUDFARi&categoryType=CODE&problemTitle=&orderBy=RECOMMEND_COUNT&selectCodeLang=ALL&select-1=3&pageSize=10&pageIndex=4
# 14178. 1차원 정원 [D3] -> Greedy
# 
# <Greedy인 이유?>
# 0. 최소한의 분무기 수를 구하는 문제
# 
# ----------------------------------------------------------------------------
import sys
import math 
input = sys.stdin.readline


TC = int(input())
answer = []

def Check(N,D):
    global answer
    num = 0
    num = math.ceil(N/(2*D+1))

    answer.append(num)


for test_case in range(TC):
    N, D = map(int, input().split())
    Check(N,D)

# 출력
for i in range(TC):
    print('#{} {}'.format(i+1, answer[i]))

# ----------------------------------------------------------------------------


