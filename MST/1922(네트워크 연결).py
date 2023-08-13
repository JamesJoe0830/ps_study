# https://www.acmicpc.net/problem/1922
# 1922. 네트워크 연결 [🥇 골드 4]
# 📚 알고리즘 분류: 최소 스패닝 트리 [Kruskal 알고리즘, Prim 알고리즘]
# ⏰ 걸린 시간 : 12분
# 
# [문제 핵심 포인트]
# 0. 모든 컴퓨터를 연결하는데 필요한 최소비용을 출력하라. 모든 컴퓨터를 연결할 수 없는 경우는 없다.
# 
# [최소 스패닝 트리 알고리즘 푼 근거 및 회고]
# 문제 조건에서 : 모든 컴퓨터 사이에 경로가 항상 존재한다. => 모든점 연결, 최소 연결 거리
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
input = sys.stdin.readline

N = int(input())
M = int(input())
graph=[[] for _ in range(N+1)]
visited = [0 for _ in range(N+1)]

for i in range(M):
    a,b,c = map(int,input().split())
    graph[a].append((c,b)) # heapq특성상 가중치를 기준으로 정렬 하므로 이렇게 넣어준다.
    graph[b].append((c,a))

def prim():
    q = []
    q.append((0,1)) # heapq특성상 가중치를 기준으로 정렬 하므로 이렇게 뽑는다.
    answer = 0 
    while q:
        len, node = heapq.heappop(q)
        if visited[node] == 0 :
            visited[node] = 1
            answer +=len
            for next_len,next_node in graph[node]:
                heapq.heappush(q,(next_len,next_node))
    return answer

print(prim())

# -------------------------------------------------------------------------------------