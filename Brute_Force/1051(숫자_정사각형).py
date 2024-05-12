import sys
N, M = map(int, sys.stdin.readline().split())
graph = [[0]*M for i in range(N)]
for i in range(N):
    a = sys.stdin.readline()
    for j in range(M):
        graph[i][j] = int(a[j])
print(graph)
line, a, b=0, 0, 0
for i in range(M):
    for j in range(i+1,M):
        if graph[0][i] ==graph[0][j]:
            True
            a = i
            b = j 
            line = j-i+1
            if graph[line-1][a]==graph[line-1][b]:
                print((j-i+1)**2)