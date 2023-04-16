# https://www.acmicpc.net/problem/11047 -> 동전 0 (실버4) Greedy
# <풀이 방법>
#  while문 돌면서 for 문에서 coins 리스트값을 뺐을때 몫을 곱해주면서 cnt 더해줌 

import sys
input = sys.stdin.readline

N, K = map(int,input().split())
cnt = 0
coins = [int(input()) for _ in range(N)]
coins.sort(reverse=True)
# print(coins)

while True:
    if K == 0:
        print(cnt)
        break

    quotient = 0 # 몫을 의미함
    for n in range(N):
        if K -coins[n]>=0:
            quotient=K //coins[n]  
            K = K - quotient*coins[n]
            cnt = cnt + quotient
            break

