# https://www.acmicpc.net/problem/7576
# 7576. 토마토 [🥇 골드 5] 
# ⏰ 걸린 시간 :1시간 10분
#
# [주의 : visited 필요 없다!]
# 0. 바로 graph에 layer에 대한 가중치를 더해주면 된다.
# 
# 
# [BFS 알고리즘로 푼 근거 및 회고]
# ✅ 트리 구조에서 Layer를 탐색하는 것이다. -> BFS에 적합하다.
# 0. 토마토는 1인 것에서 부터 익는것을 결정한다. 1이 여러개 일때 익는 시점은 같다. 
# 1. Queue에 1인것 모두 다 넣고 Que를 빼주면서 시작하면 된다.
# ---------------------------------------------------------------------------
import sys
from collections import deque

input = sys.stdin.readline
# M: 가로칸의 개수, N: 세로칸의 개수
M, N = map(int, input().split())

graph = [list(map(int, input().split())) for i in range(N)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
Que = deque()

# M(가로 : x ):6 N(세로, y):4
# 먼저 Que에 1인거 다 넣어주기 (익는 시점은 1이 있는게 다 동일하므로)
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            Que.append((i, j))
#BFS 시작
while Que:
    (x, y) = Que.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx <= N-1 and 0 <= ny <= M-1:
            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                Que.append((nx, ny))

day = 0
answer = 0
for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            answer = -1
            break
        else:
            day = max(day, graph[i][j])
if answer != -1:
    #날짜 1일부터 시작했으므로 
    answer = day-1
print(answer)
