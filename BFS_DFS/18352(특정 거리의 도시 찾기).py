# https://www.acmicpc.net/problem/18352
# 18352. 특정 거리의 도시 찾기 [🥈 실버 2]
#  ⏰ 걸린 시간 : 50분
# 시간복잡도 : BFS -> O(N+M)
# [⚡️ 주의 사항]
# 0. 시간초과 발생 -> visited를 set()으로 설정하지 않아서 시간초과가 발생했다. 
# 1. recursion DFS로 접근했는데 각 계층을 누적해서 거리를 표현하는게 어려웠다.
# 2. Layer 문제는 BFS로 풀자
# 
# [BFS 알고리즘로 푼 근거 및 회고]
# ✅ 거리를 이전의 값을 누적해서 더해간다 => Layer 문제
# 0. distance 계산을 하는 문제지만 두가지 고려해야할 부분이 있다.
# 1. 누적을 하되 이전에 방문한 적이 있는 노드는 visited에 넣어 관리한다. (이유: 발견은 최소의 거리를 구하기 때문)
# 2. Que에 (X :start)를 넣어서 빌때까지 BFS를 돌린다.
# ------------------------------------------------------------
import sys
from collections import deque
input = sys.stdin.readline
N, M, K, X = map(int, input().split())
# N: N개의 지점, M: M개의 연결, X : start 지점,
graph = [[] for _ in range(N+1)]
Que = deque()
visited = set()

distances = [0]*(N+1)
for i in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
Que.append(X)
visited.add(X)

while Que:
    node = Que.popleft()
    for next in graph[node]:
        if next not in visited:
            Que.append(next)
            visited.add(next)
            distances[next] = distances[node]+1

if K in distances:
    for destination in range(1,N+1):
        if distances[destination] ==K:
            print(destination)
else:
    print(-1)
             



# [풀이방법 0.]------------------------------------------------------------
# ⏰ 시간초과 발생 -> visited를 set()으로 설정하지 않아서 시간초과가 발생했다.
# import sys
# from collections import deque
# input = sys.stdin.readline
# N, M, K, X = map(int, input().split())
# # N: N개의 지점, M: M개의 연결, X : start 지점,
# graph = [[] for _ in range(N+1)]
# Que = deque()
# visited = [] 

# distances = [0]*(N+1)
# for i in range(M):
#     x, y = map(int, input().split())
#     graph[x].append(y)
# Que.append(X)
# visited.append(X)

# while Que:
#     node = Que.popleft()
#     for next in graph[node]:
#         if next not in visited:
#             Que.append(next)
#             visited.append(next)
#             distances[next] = distances[node]+1

# if K in distances:
#     for destination in range(1,N+1):
#         if distances[destination] ==K:
#             print(destination)
# else:
#     print(-1)
             
