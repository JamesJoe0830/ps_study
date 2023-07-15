# https://www.acmicpc.net/problem/14501 -> 퇴사(실버3) -> 브루트 포스
#  <브루트포스인 근거 ?> -> 이거 DP를 이용해야 하는가 .. ?
# 
# <문제 접근 방법> 
# 
# --------------------------------------------------------------------------
import sys
input =sys.stdin.readline

N=int(input())
Task = [0]*(N+1)
Pay = [0]*(N+1)
for n in range(1,N+1):
    T, P = map(int,input().split())
    Task[n] = T
    Pay[n] = P

d = 1
answer = 0
while True:
    print("answer",d,answer)

    if d>N :
        print(answer)
        break

    money=Pay[d]
    if d+Task[d]-1 <= N :
        for i in range(d,d+Task[d]):
            if Task[d]+d-1 >= Task[i]+i-1 and Pay[d] < Pay[i]:
                d = i
                Task[d]=Task[i]
                Pay[d]=Pay[i]
                money = Pay[i]
        else:
            d = d+Task[d] -1
    answer += money
    d+=1 

    