# https://www.acmicpc.net/problem/2164
# 2164. 카드2 [🥈 실버 4]
# 📚 알고리즘 분류: 큐(Queue)
# ⏰ 걸린 시간 : 10분
# 
# [문제 풀이]
# 0. Queue가 한개 남을때까지만 돈다.
# 1. 짝수일때만 뒤로 다시 넣어준다.
# 2. 홀수일때만 버린다.
# 
# ------------------------------------------------------------------


import sys
from collections import deque
input=sys.stdin.readline
N =int(input())
Q = deque()
for i in range(1,N+1):
    Q.append(i)
cnt = 1
while len(Q) > 1:
    num = Q.popleft()
    if cnt % 2 == 0:
        Q.append(num)
    cnt +=1
print(Q[0])