# https://www.acmicpc.net/problem/2217 -> 로프 (실버 4) 브루트 포스
# <문제 풀이>
# 0. 선택된 로프의 무게중 가장 작은것을 로프 개수만큼 버틸 수 있음 
# 1. answer의 초기 값을 지정하고 계속 업데이트 하는 방식으로 할 것
# 
# -----------------------------------------------------------------------------
import sys
input = sys.stdin.readline

N = int(input())
i = 0

weightList = []


for n in range(N):
    weight = int(input())
    weightList.append(weight)
weightList.sort()

# 문제 포인트 : 계속 answer값을 update 해주는 방식으로 
answer = weightList[0]*N 
for i in range(1,len(weightList)):
    if answer >= weightList[i]*(N-i):
        answer = answer
    else:
        answer = weightList[i]*(N-i)


print(answer)
# -----------------------------------------------------------------------------
