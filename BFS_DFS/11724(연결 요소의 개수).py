# https://www.acmicpc.net/problem/11724 (실버 2) -> 오답 필요
# <recursion DFS로 푼 근거>
# 0. 재귀 함수를 돌면서 연결된 요소들을 하나로 보고 깊이 탐색이 유리
# 1.
# <주의사항>
# 0. 메모리 초과에 유의할 것 

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, M = map(int,input().split())
graph =[[] for _ in range(N+1)]
visited = list()
Connect = 0 # 연결 요소의 개수

for _ in range(M): # [[], [2, 5], [1, 5], [4], [3, 6], [2, 1], [4]]
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

# recursion DFS
def DFS(v): 
    visited.append(v)
    for node in graph[v]:
        if node not in visited :
            visited.append(node)
            DFS(node)

for i in range(1, N+1):
        if i not in visited:
             DFS(i)
             Connect +=1 
print(Connect)


# <메모리 초과>
# graph =[[0]*(N+1) for _ in range(N+1)]

# for _ in range(M):
    # graph[row][col] = 1
    # graph[col][row] = 1

#recursion DFS
# def DFS(v): 
#     visited.append(v)
#     for node in range(N+1):
#         if graph[v][node] == 1 and node not in visited :
#             visited.append(node)
#             DFS(node)

# for i in range(N+1):
#     for j in range(N+1):
#         if graph[i][j] == 1 and i not in visited:
#             DFS(i)
#             Connect +=1 
# print(Connect)