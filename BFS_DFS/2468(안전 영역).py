# https://www.acmicpc.net/problem/2468
# 2468. 안전 영역 [🥈 실버 1]
# 
# 
# 
# [recursion DFS로 푼 근거]
# ✅ 재귀 함수를 돌면서 연결된 요소들을 하나로 보고 깊이 탐색이 유리
# 0. DFS 알고리즘 특성 깊이 탐색을 한다.
# 1. 해당 문제는 DFS는 안전 영역을 체크하는 것이다.
# 2. 깊게 탐색후 하나의 영역을 다 체크하고 나오는 것이 목표이기 때문에 DFS가 적합하다고 판단했다.
# ---------------------------------------------------------------------------
import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

N = int(input())
graph = []
max_water = 0
dx = [0,0,-1,1]
dy = [-1,1,0,0]

for i in range(N):
    row = list(map(int,input().split()))
    max_water = max(max_water,max(row))
    graph.append(row)


# recursion DFS
def DFS(x,y,water):
    visited[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx <= N-1 and 0 <= ny <= N-1 :
            if visited[nx][ny] == 0 and graph[nx][ny] > water:
                DFS(nx,ny,water)

safety_area=[]
for water in range(0,max_water+1):
    cnt = 0
    visited = [[0]*N for i in range(N)]
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0 and graph[i][j] > water :
                cnt += 1
                DFS(i,j,water)
    safety_area.append(cnt)

print(max(safety_area))
# ---------------------------------------------------------------------------