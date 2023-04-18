# https://www.acmicpc.net/problem/7562 -> 나이트의 이동(실버 1) -> BFS & DFS 
# [____ Layer 체크 적용하기 너무 좋은 문제___ ]

# <BFS로 푼 근거 >
# 0. layer를 표시하기 너무 좋다.
# 1. dfs로 풀면 깊게 들어갔다가 나와야하는 구현의 허점이 있다.
# <문제 풀이>
# 0. Layer에 관한 문제이다 결국엔
# 1. 갈 수 있는 방향에 대해 8가지의 방향을 표시해주고 dx, dy로 설정
# 
# --------------------------------------------------------------------------
import sys
input = sys.stdin.readline
from collections import deque
t = int(input())


dx = [-1,1,-1,1,2,-2,2,-2]
dy = [-2,-2,2,2,1,1,-1,-1]
answer = []

def BFS():
    Que.append((str_x,str_y))
    while Que:
        (x,y) = Que.popleft()
        if (end_x,end_y) == (x,y):
            answer.append(graph[x][y])
            break

        for i in range(8):
            nx_x = x + dx[i]
            nx_y = y + dy[i]
            if N > nx_x >= 0 and N > nx_y >=0 and graph[nx_x][nx_y] ==0 :
                graph[nx_x][nx_y] = graph[x][y] + 1 #여기가 layer를 확인하기 위한 부분
                Que.append((nx_x,nx_y))
            
for _ in range(t):
    N = int(input())
    graph = [[0]*N for _ in range(N)]
    str_x,str_y = map(int,input().split())
    end_x,end_y = map(int,input().split())
    graph[str_x][str_y] = 1

    Que = deque()
    BFS()



# 출력
for i in range(t):
    print(answer[i]-1)

# --------------------------------------------------------------------------
