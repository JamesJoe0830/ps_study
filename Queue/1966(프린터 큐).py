# https://www.acmicpc.net/problem/1966
# 1966. 프린터 큐 [🥈 실버 3]
# 📚 알고리즘 분류: 큐(Queue)
# ⏰ 걸린 시간 : 15분
# 
# [문제 풀이]
# 0. Queue가 빌때까지 돌면서 뽑는데
# 1. Que중에서 중요도가 가장 높은 값이 아니면 뒤로 보내고
# 2. 뽑은 녀석이 가장 중요도가 높은 값이면 뽑은 순번을 매기고 뽑아버린다.
# 3. 뽑았을때 index가 M과 일치하면 순번을 출력함
# ------------------------------------------------------------------
import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

for tc in range(T):
    N, M = map(int, input().split())
    importants = list(map(int, input().split()))
    Q = deque()
    for i in range(N):
        Q.append((importants[i],i))
    cnt = 0

    while Q:
        max_value = max(Q, key=lambda x:x[0])[0] # 중요도가 가장 높은지 확인하기 위한 것
        important, idx = Q.popleft()
        if important != max_value: # 중요도가 가장 높은 값이 아닐때 뒤로 보냄
            Q.append((important, idx))
        else:                      # 중요도가 가장 높은 값이라면 뽑고 뽑은 번호를 정함
            cnt +=1
            if idx == M:
                print(cnt)
                break
# ------------------------------------------------------------------





