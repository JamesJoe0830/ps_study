# https://www.acmicpc.net/problem/1049 -> 기타줄 (실버 4) -> Greedy
# <Greedy 인 이유>
# 0. 가장 적게 돈이 드는 경우를 고르는 것임
# 
# 
# 
# -----------------------------------------------------------------------------
import sys

input= sys.stdin.readline

N, M = map(int,input().split())
pakage, single  = [], []
answer = 0
for m in range(M):
    pk, one = map(int,input().split())
    pakage.append(pk)
    single.append(one)

while True :
    if N == 0 : 
        print(answer)
        break
    if N>6 :
        if min(pakage) >= 6* min(single):
            answer += 6*min(single)
            N -= 6
        else: 
            answer +=  min(pakage)
            N -= 6
    else:
        answer += min(min(pakage),N*min(single))
        N -= N
# -----------------------------------------------------------------------------


