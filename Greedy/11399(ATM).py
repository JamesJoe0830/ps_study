# https://www.acmicpc.net/problem/11399 -> ATM(실버 4) Greedy
# <문제 풀이 방법>
# 0. 작은 값들 부터 더해지는게 이득이기 때문에 오름차순 정렬
# 1. while문 돌리기 
# -----------------------------------------------------------------------------
import sys
input = sys.stdin.readline

N= int(input())
t = 0
time = 0
ATM = list(map(int,input().split()))
ATM.sort()
while True:

    for i in range(0,t):
        time += ATM[i]
    t+=1

    if t > N:  #종료 조건
        print(time)
        break
# -----------------------------------------------------------------------------
