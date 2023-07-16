# https://www.acmicpc.net/problem/2606
# 2606. 바이러스 [🥈  실버 3] 
# ⏰ 걸린 시간 :20분
# 
# [recursion DFS로 푼 근거]
# ✅ 재귀 함수를 돌면서 연결된 요소들을 하나로 보고 깊이 탐색이 유리
# 0. DFS 알고리즘 특성 깊이 탐색을 한다.
# 1. 해당 문제의 DFS는 바이러스 컴퓨터를 체크하는 것이다.
# 2. 깊게 탐색후 바이러스 감염을 다 체크하고 나오는 것이 목표이기 때문에 DFS가 적합하다고 판단했다.
# ---------------------------------------------------------------------------

import sys
input = sys.stdin.readline
# N : 컴퓨터 대수, M:직접 연결되어 있는 컴퓨터 쌍의 수
N = int(input())
M = int(input())
graph = [[0]*(N+1)for i in range(N+1)]
visited,needvisit = [], []

for i in range(M):
    a, b = map(int,sys.stdin.readline().split())
    graph[a][b] = 1
    graph[b][a] = 1

# recursion DFS
def DFS(n):
    visited.append(n)
    next = 0

    for i in range(N+1):
        if graph[n][i] == 1 and i not in visited and i not in needvisit:
            needvisit.append(i)
    if needvisit:
        next = needvisit.pop()
        DFS(next)
    if not needvisit: # 재귀 끝내는 조건 
        return False
DFS(1)
print(len(visited)-1)
# ---------------------------------------------------------------------------