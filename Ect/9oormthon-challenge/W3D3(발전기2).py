# https://level.goorm.io/exam/195695/%EB%B0%9C%EC%A0%84%EA%B8%B0-2/quiz/1
import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int,input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]

buliding_nums = set()
for row in graph:
    for num in row:
        buliding_nums.add(num)

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
Q = deque()


def BFS(x,y,nums,B_cnt):
    Q.append((x,y))
    visited[x][y] = 1
    while Q:
        x,y = Q.popleft()
        B_cnt +=1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx <N and 0<= ny <N:
                if graph[nx][ny] == nums and visited[nx][ny] == 0:
                    Q.append((nx,ny))
                    visited[nx][ny] =1
    return B_cnt



answer =[]
for nums in buliding_nums:
    Villa = 0
    for i in range(N):
        for j in range(N):
            if graph[i][j] == nums and visited[i][j] == 0 :
                B_cnt = 0
                if BFS(i,j, nums,B_cnt) >= K :
                    Villa +=1
    answer.append((Villa,nums))
answer.sort(reverse=True)
max_answer = max(answer, key=lambda x: x[0])[1]
print(max_answer)
