import sys
N, M, V = map(int, sys.stdin.readline().split())
graph = [[0]*(N+1) for i in range(N+1)]
needvisit, visited = [], []
needvisit2, visited2 = [], []

for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a][b] = 1
    graph[b][a] = 1
# print(arr)
def dfs(n):
    if len(visited)==N: # 종료 조건을 만듦 visited길이가 N일때 멈춤
        return
    pop_need=0
    for i in range(N+1):    #i는 각 노드 / N+1까지 해준 이유 0부터 시작이므로
        if graph[n][i]==1 and i not in visited:
            needvisit.append(i)
    # print('ndvisit',needvisit)
    if needvisit : # needvisit에 원소가 있다면 0번째 인덱스 뽑아서 저장
        pop_need=needvisit.pop(0)

    needvisit.clear() #dfs 라서 비워주는 것으로 계속 needvisit을 리셋
    visited.append(n)
    dfs(pop_need)
    return visited

   
def bfs(n):
    if len(visited2)==N: # 종료 조건을 만듦 visited길이가 N일때 멈춤
        return
    pop_need=0
    for i in range(N+1):
        if graph[n][i]==1 and i not in visited2:
            needvisit2.append(i)
    if needvisit2 :
        pop_need=needvisit2.pop(0)
    visited2.append(n)
    bfs(pop_need)
    return visited2

print(dfs(V))
print(bfs(V))

