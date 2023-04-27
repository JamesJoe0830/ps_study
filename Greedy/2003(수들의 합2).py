# https://www.acmicpc.net/problem/2003 -> 수들의 합 2(실버 4) Greedy
# <풀이 방법>
# 0. 번째를 증가하면서 합을 구하고 그때마다 M과 확인할 것
# while문을 쓰면 좋을 것 같다. 

# --------------------------------------------------------------------------
import sys
input = sys.stdin.readline

N, M = map(int,input().split())
num =list(map(int,input().split()))
count = 0
i=0

while i<N:
    sum=0 # sum을 초기화
    for n in range(i,N): #i를 증가하면서 시작 자리수 위치 바꿔주기
        sum += num[n]
        if sum == M :
            count += 1
        elif sum >M:
            break
    i +=1 

print(count)
# --------------------------------------------------------------------------

