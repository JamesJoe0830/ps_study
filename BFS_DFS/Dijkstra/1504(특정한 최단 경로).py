# https://www.acmicpc.net/problem/1504
# 1504. 특정한 최단 경로 [🥇 골드 4] -> 🔥 오답 필요
# 📚 알고리즘 분류: 다익스트라 알고리즘
# ⏰ 걸린 시간 : 110분 (주의사항에 기재함)
# 시간복잡도 : 다익스트라 -> O(ElogV) : EV인데 우선순위 큐 사용해주면 탐색이 logV로 줄어든다.
#
# 
# [💡 주의할점]
# 이경우 생길 수 있는 경로는 2가지 이다.
# 시작정점 -> stop1 -> stop2 -> 도착정점
# 시작정점 -> stop2 -> stop1 -> 도착정점
# 
# [다익스트라 알고리즘 푼 근거 및 회고]
# ✅ 전형적인 최단 경로 문제이다.
# 다익스트라 : 한 정점에서 모든 정점까지의 거리를 계산함
# 0. 가는 길을 택하는데 최소의 거리 길이를 택하여서 가야하기 때문이다.
# 1. 플로이드 워셜의 경우는 시간 복잡도가 O(V^3)인데 D의 입력이 10,000이기 때문에 2초를 초과 할 수 있다.
# 
# 
# heap 은 기본적으로 최소힙 자료구조를 제공한다.
# ------------------------------------------------------------
import sys
import heapq
input = sys.stdin.readline

N ,E =map(int, input().split())
INF = int(1e9)
graph = [[] for _ in range(N+1)]

for i in range(E):
    s, e, l = map(int, input().split())
    graph[s].append((e,l))
    graph[e].append((s,l))
v1,v2 = map(int, input().split())

def dijkstra(start,end):
    path = [INF]*(N+1)
    q = []
    heapq.heappush(q,(0,start))
    path[start]=0

    while q:
        length, now = heapq.heappop(q)
        if path[now] < length:
            continue
        
        for e,l in graph[now]:
            now_length = l + length
            if now_length < path[e]:
                path[e] = now_length
                heapq.heappush(q,(now_length,e))
    return path[end]


# 🔥 주의사항 볼 것
path1 = dijkstra(1,v1) +dijkstra(v1,v2) +dijkstra(v2,N)
path2 = dijkstra(1,v2) +dijkstra(v2,v1) +dijkstra(v1,N)
if path1 >= INF and path2 >= INF:
    print(-1)
else:
    print(min(path1,path2))