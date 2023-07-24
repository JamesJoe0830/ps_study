# https://www.acmicpc.net/problem/1916
# 1916. 최소비용 구하기 [🥇골드 5] -> 🔥 오답 필요
# 📚 알고리즘 분류: 다익스트라 알고리즘
# ⏰ 걸린 시간 : 40분 (1446 지름길 풀고 풀어서 그런지 풀리긴 하는데.. 연습 필요)
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
import heapq
import sys
input = sys.stdin.readline

INF = int(1e9) #무한을 의미하는 값으로 10억을 설정
# N : 도시의 개수 , M: 버스의 개수
N = int(input())
M = int(input())

#출발 도시번호, 도착지 도시번호, 버스 비용
cost = [INF] * (N+1) #[INF, INF, INF,INF,INF]
graph = [[] for _ in range(N+1)]
for i in range(M):
    s,e, c = map(int,input().split()) # s: start, e: end, c: cost
    graph[s].append((e,c))
start, end = map(int, input().split())
# print(graph)
# [[], [(2, 2), (3, 3), (4, 1), (5, 10)], [(4, 2)], [(4, 1), (5, 1)], [(5, 3)], []]
def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    cost[start] = 0 #시작 시점의 비용은 0이므로
    while q:
        # print("⏰",q)

        pay, now = heapq.heappop(q)

        if cost[now] < pay: # 비교하기 위한 비용이 여태까지의 cost들중 선정된 비용보다 크면 아래 생략 [⏰ 이줄 없으면 시간초과 발생]
            continue

        for e, c in graph[now]:
            now_cost = pay + c
            # print("🌙",now_cost,pay,c)
            if now_cost < cost[e]: # 도착했지점까지의 비용 < 도착지의 비용 (즉, 더 싼 비용 지불한 경우)
                cost[e] = now_cost
                heapq.heappush(q,(now_cost,e))

dijkstra(start)
print(cost[end])