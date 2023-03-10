import sys
from collections import deque

input =sys.stdin.readline
N, M =map(int,input().split())
graph = [[] for _ in range(N+1)]
#  # 방문한 노드 체크


for i in range(M):
    a,b = map(int,input().split())
    graph[b].append(a) # [[], [3], [3], [4, 5], [], []]

# BFS
def BFS(v):
    Que = deque([v])
    visited = [0]*(N+1)
    visited[v] =1
    count =0 
    while Que:
        v= Que.popleft() # deque을 queue처럼 사용하기 위해 왼쪽에서 부터 pop
        for i in graph[v]:
            if not visited[i]:
                Que.append(i)
                visited[i] =1
                count+=1
    # print(count)
    return count
result = []
max_value = 0 
for i in range(1,N+1):
    cnt= BFS(i)
    if cnt>max_value:
        result =[i]
        max_value = cnt
    elif cnt == max_value:
        result.append(i)
        max_value=cnt
for i in result:
    print(i, end=' ')


# <DFS로 접근시 메모리 초과 발생>
# # print('graph',graph)
# #recursion DFS
# def DFS(x,y):
#     visited.append(y) #방문한 곳에 [3,4,5]이런식으로 넣어주기
#     for i in range(N+1):
#         if graph[y][i] ==1:
#             DFS(y,i)
#     print(visited)

# cnt =0
# for i in range(N+1):
#     cnt=len(visited)
#     hacked.append(cnt)
#     visited =[]
#     for j in range(N+1):
#         if graph[i][j] ==1 :
#             DFS(i,j)
# hacked.pop(0)
# print(hacked)
# max_value = max(hacked)
# for i in range(len(hacked)):
#     if max_value == hacked[i]:
#         print(i, end = ' ',flush=True)
