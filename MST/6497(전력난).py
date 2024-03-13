# https://www.acmicpc.net/problem/6497
# 6497. 전력난 [🥇 골드 4]
# 📚 알고리즘 분류: 최소 스패닝 트리 [Kruskal 알고리즘, Prim 알고리즘]
# ⏰ 걸린 시간 : 16분
# 
# [문제 핵심 포인트]
# 0. 모든 행성을 연결하는데 필요한 최소비용을 출력하라. 모든 행성을 연결할 수 없는 경우는 없다.
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
from heapq import heappop, heappush
input = sys.stdin.readline


# m: 집의 수, n: 길의 수
while True:
  m, n = map(int ,input().split())
  if m == 0 and n == 0 :
    break
  town = [[] for _ in range(m)]
  visited = [0]*m
  total = 0

  for i in range(n):
    x, y ,z  = map(int,input().split())
    town[x].append((z,y))
    town[y].append((z,x))
    total += z


  def mst():
    q = []
    q.append((0,0))
    use_cost = 0
    while q :
      cost, node = heappop(q)
      if visited[node] == 0 :
        use_cost += cost
        visited[node] = 1
        for next_cost, next in town[node]:
          if visited[next] == 0:
            heappush(q,(next_cost,next))
    return (total-use_cost)

  print(mst())

# -------------------------------------------------------------------------------------