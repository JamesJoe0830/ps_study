# https://www.acmicpc.net/problem/16953 
# <BFS로 푼 근거>
# 0. 가장 빨리 찾는 경로
# 1. 방문한 곳 plunning 처리해주기 위함 
# <주의 사항>
# 0. 최대가 1억 이기 때문에 [0] * (10**9) 이렇게하면 메모리와 시간초과 가능성 있음
# 1. 방문한 곳 체크 
# 2. while 안에 for 문을 도는 동안은 같은 layer 이므로 cnt 증가 없도록 할것(que에 넣고 다시 -1처리)
# 3. 찾았을때 못찾았을때를 토글로 구분

import sys
from collections import deque 
input = sys.stdin.readline

A, B = map(int, input().split())
Que = deque()
visited = list()

#BFS 
def BFS(c,v):
    Que.append([c,v])
    found =False

    while Que:
        cnt, now = Que.popleft()
        visited.append(now)
        if now >int(10**9):
            continue
        if now == B:
            print(cnt)
            found =True
            break
        for next in (2*now, int(str(now)+'1')):
            if next not in visited and 1<= next <= 10**9:
                cnt +=1
                Que.append([cnt,next])
                cnt -=1
    if not found:
        print(-1)

BFS(1,A)