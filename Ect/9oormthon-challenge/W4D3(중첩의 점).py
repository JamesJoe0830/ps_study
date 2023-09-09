# https://level.goorm.io/exam/195700/%EC%A4%91%EC%B2%A9-%EC%A0%90/quiz/1
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[[0, 0] for _ in range(N+1)] for _ in range(N+1)]

# d: direction

def DFS(y,x,dy,dx):
    if dy !=0 : 
        graph[y][x][0] +=1
    elif dx != 0:
        graph[y][x][1] +=1
    nx = x + dx
    ny = y + dy
    if 0 < nx < N+1 and 0 < ny < N+1:
        DFS(ny,nx,dy,dx)

dX = [0, 0, -1, 1]
dY = [-1, 1, 0, 0]

for i in range(M):
    y, x, d = input().split()
    if d == 'U':
        dy = dY[0]
        dx = dX[0]
    elif d == 'D':
        dy = dY[1]
        dx = dX[1]
    elif d == 'L':
        dy = dY[2]
        dx = dX[2]
    elif d == 'R':
        dy = dY[3]
        dx = dX[3]
    
    DFS(int(y),int(x),dy,dx)
answer = 0
for row in graph:
    for y,x in row:
        if y !=0 and x != 0:
            answer += y*x
print(answer)

