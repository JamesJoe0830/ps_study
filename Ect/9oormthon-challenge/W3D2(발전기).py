# https://level.goorm.io/exam/195694/%EB%B0%9C%EC%A0%84%EA%B8%B0/quiz/1
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
Q = deque()
def BFS(i,j):
    Q.append((i,j))
    visited[i][j] = 1

    while Q:
        x,y = Q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if graph[nx][ny] == 1 and visited[nx][ny] == 0:
                    Q.append((nx,ny))
                    visited[nx][ny] = 1



power_plant = 0 
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1 and visited[i][j] == 0:
            power_plant += 1
            BFS(i,j)
            
print(power_plant)

# def DFS(x,y):
#     visited[x][y] = 1
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if 0 <= nx < N and 0 <= ny < N:
#             if graph[nx][ny] == 1 and visited[nx][ny] == 0:
#                 DFS(nx,ny)


# power_plant = 0 
# for i in range(N):
#     for j in range(N):
#         if graph[i][j] == 1 and visited[i][j] == 0:
#             power_plant += 1
#             DFS(i,j)
            
# print(power_plant)