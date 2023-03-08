import sys

N, M, V = map(int, sys.stdin.readline().split())
graph = [[0]*(N+1) for i in range(N+1)]
visited = [0]*(N+1)

for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a][b] = 1
    graph[b][a] = 1
# DFS
def DFS(n):
    visited[n] = 1 # 방문한곳 1로 체크
    print (n, end=' ')
    for i in range(N+1):    #i는 각 노드 / N+1까지 해준 이유 0부터 시작이므로
        if graph[n][i]==1 and visited[i] ==0:
            DFS(i)

#BFS
def BFS(n):
    need_visit = []
    need_visit.append(n) # 앞으로 방문해야되는 곳 queue에 입력
    visited[n] = 0  # DFS함수에서 1로 설정되어있으므로 거꾸로 방문한 곳 0으로 설정
    while need_visit :  # 큐가 빌 때까지
        n = need_visit.pop(0)   # 맨 앞의 노드부터 방문
        print(n, end = ' ')
        for i in range(1, N+1) :
            if visited[i] == 1 and graph[n][i] == 1 :
                visited[i] = 0
                need_visit.append(i)

DFS(V)
print()
BFS(V)

