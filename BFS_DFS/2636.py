# https://www.acmicpc.net/problem/2636 치즈 (골드 4)
# <주의사항>
# 바로 근처가 0 이면서 1인 녀석을 탐색한다. -> DFS 쓰면 가장자리 탐색이 어려움 그냥 계속 깊게 탐색하므로 

import sys
input = sys.stdin.readline

row, col = map(int,input().split())

graph = [list(map(int,input().split())) for _ in range(row)]
check_list = [[0]*col for _ in range(row)]
print(graph)
print(check_list)

def DFS (x,y):
    Find=False
    check_list[x][y] == 1
    # graph[x][y] == 0
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
    if graph[nx][ny]

    if check_list[x][y] == 0 and graph[x][y] ==1:
        DFS(nx,ny)

    


for i in range(row):
    for j in range(col):
        if graph[i][j] == 1 and check_list[i][j] == 0:
            DFS(i,j)
