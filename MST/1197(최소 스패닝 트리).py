# https://www.acmicpc.net/problem/1197
# 1197. 최소 스패닝 트리 [🥇 골드 4]-> 🔥 오답 필요
# 📚 알고리즘 분류: 최소 스패닝 트리 [Kruskal 알고리즘, Prim 알고리즘]
# ⏰ 걸린 시간 : 시간초과 (MST 알고리즘으로 처음)
# 
# 
# [최소 스패닝 트리 알고리즘 푼 근거 및 회고]
#  0. 모든 정점이 다연결 되어 있고 사이클이 없다!
#  1. Kruskal알고리즘은 간선들을 정렬해야하기 때문에 간선이 적으면 Kruskal, 많으면 Prim을 선택한다.
# 
# 📚 [Prim]
# 0. 임의의 정점을 선택
# 1. 해당 정점에서 갈 수 있는 간선을 minheap에 넣는다.
# 2. 최소값을 뽑아 해당 정점을 방문 안했다면 선택한다.
# 비슷한 알고리즘으로 다익스트라 알고리즘이 있다.
# 🍯 다익스트라는 전체 요소를 연결하는 것이 아닌 한 정점에서 다른 정점으로 가는 가장 짧은 방법을 구할 때 사용한다.
# -------------------------------------------------------------------------------------

import sys
import heapq
input=sys.stdin.readline

V, E = map(int,input().split())

graph =[[] for _ in range(V+1)]
visited=[0 for _ in range(V+1)]


for i in range(E):
    A,B,C = map(int,input().split())
    graph[A].append([C,B])
    graph[B].append((C,A))

def prim():
    q = []
    answer,cnt = 0, 0
    q.append((0,1)) # heapq특성상 가중치를 기준으로 정렬 하므로 이렇게 넣어준다.
    while q:
        if cnt == V:
            break

        node, len = heapq.heappop(q) # heapq특성상 가중치를 기준으로 정렬 하므로 이렇게 뽑는다.
        if visited[node] == 0:
            visited[node] = 1
            answer += len
            cnt+=1
            for next_len, next_node in graph[node]:
                heapq.heappush(q, (next_len,next_node))
    return print(answer)
prim()

# -------------------------------------------------------------------------------------

