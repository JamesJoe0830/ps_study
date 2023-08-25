import sys

N, K = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(N)]

dx = [-1, 1, -1, 1, -1, 1, 0, 0]
dy = [1, -1, -1, 1,  0 ,0 ,-1, 1]
answer = 0

def check(x,y):
    global answer
    cnt = 0
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<= nx <N and 0<= ny <N :
            if graph[nx][ny] == 1:
                cnt+=1
    if cnt == K:
        answer +=1

    return answer


for x in range(N):
    for y in range(N):
        if graph[x][y] == 0 :
            check(x,y)
print(answer)
