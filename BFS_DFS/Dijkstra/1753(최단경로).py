# https://www.acmicpc.net/problem/1753
# 1753. 최단경로 [🥇골드 4] -> 🔥 오답 필요 
# ✨ 비슷한 문제  [1916:최소비용 구하기]
# 📚 알고리즘 분류: 다익스트라 알고리즘
# ⏰ 걸린 시간 : 43분 (1446 지름길 풀고 풀어서 그런지 풀리긴 하는데.. 연습 필요)
#
# [다익스트라 알고리즘 푼 근거 및 회고]
# ✅ 전형적인 최단 경로 문제이다.
# 다익스트라 O(ElogV) : 한 정점에서 모든 정점까지의 거리를 계산함
# 0. 가는 길을 택하는데 최소의 비용을 택하여서 가야하기 때문이다.
# 1. 플로이드 워셜의 경우는 시간 복잡도가 O(V^3)인데 D의 입력이 10,000이기 때문에 2초를 초과 할 수 있다.
# 
# 
# heap 은 기본적으로 최소힙 자료구조를 제공한다.
# ------------------------------------------------------------
import sys
import heapq
input = sys.stdin.readline
V, E = map(int, input().split())
K = int(input())
INF = int(1e9)
graph = [[] for _ in range(V+1)]
path = [INF] * (V+1)

for i in range(E):
    u, v, w = map(int,input().split())
    graph[u].append((v,w))

def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    path[start] = 0
    while q:

        length, now = heapq.heappop(q)

        if path[now] < length: 
            continue

        for e,l in graph[now]:
            now_length = length + l
            if now_length < path[e]:
                path[e] = now_length
                heapq.heappush(q,(now_length,e))


dijkstra(K)

# i번째 줄에 i번 정점으로의 최단 경로의 경로값을 출력
for i in range(1,V+1):
    if path[i] == INF:
        print('INF')
    else:
        print(path[i])


# ------------------------------------------------------------