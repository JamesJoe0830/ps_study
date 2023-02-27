import sys
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
graph = [[0]*(N+1)for i in range(N+1)]
visited,needvisit = [], []

for i in range(M):
    a, b = map(int,sys.stdin.readline().split())
    graph[a][b] = 1
    graph[b][a] = 1

def dfs(n):
    next = 0
    for i in range(N+1):
        if graph[n][i] == 1 and i not in visited and i not in needvisit:
            needvisit.append(i)
    visited.append(n)
    if needvisit:
        next = needvisit.pop()
        dfs(next)
    if not needvisit: # 재귀 끝내는 조건 
        return False
dfs(1)
visited.pop(0)
print(len(visited))
