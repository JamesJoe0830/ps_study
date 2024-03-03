# https://www.acmicpc.net/problem/1647
# 1647. 도시 분할 계획 [🥇 골드 4]
# 📚 알고리즘 분류: 최소 스패닝 트리 [Kruskal 알고리즘, Prim 알고리즘]
# ⏰ 걸린 시간 : 28분
# 
# [문제 핵심 포인트]
# 0. 결국엔 모든 최소 길이들 배열에서 최대 길이를 끊어 마을을 나눠주면 된다.
# 
# [최소 스패닝 트리 알고리즘 푼 근거 및 회고]
# 문제 조건에서 : 임의의 두 집 사이에 경로가 항상 존재한다. => 모든점 연결, 최소 연결 거리
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
from heapq import heappop, heappush
sys.stdin.readline

#N : 집의 개수 , M : 길의 개수

N, M = map(int,input().split())
town = [[] for _ in range(N+1)]
for _ in range(M):
  A, B, C = map(int, input().split())
  town[A].append((C,B))
  town[B].append((C,A))
visited = [0] * (N+1)

def prim():
  q = []
  q. append((0,1))
  answer = 0
  max_len = 0
  while q :
    len, node = heappop(q)

    if visited[node] == 0:
      visited[node] = 1
      max_len = max(len, max_len)
      answer += len

      for next_len, next_node in town[node]:
        if visited[next_node] == 0:
          heappush(q, (next_len,next_node))
  return print(answer - max_len)

prim()

# -------------------------------------------------------------------------------------