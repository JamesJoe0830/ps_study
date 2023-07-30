# https://www.acmicpc.net/problem/10282
# 10282. 해킹 [🥇 골드 4]
# 📚 알고리즘 분류: 다익스트라 알고리즘
# ⏰ 걸린 시간 : 48분 (다익스트라 알고리즘으로 처음 풀어봐서 어려움)
# 시간복잡도 : 다익스트라 -> O(dlogn) : dn인데 우선순위 큐 사용해주면 탐색이 logn로 줄어든다.
#   
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

tc = int(input())
#  n: 컴퓨터 개수 / d : 의존성 개수 / c: 해킹당한 컴퓨터 번호
#  a가 컴퓨터 b를 의존하며, 컴퓨터 b가 감염되면 s초 후 컴퓨터 a도 감염됨
def dijkstra(start, infection_times, graph):

    q = []
    heapq.heappush(q,(0,start))
    infection_times[start] = 0

    while q:
        time, now =heapq.heappop(q)

        if infection_times[now] < time:
            continue
        
        for a, s in graph[now]:
            now_totalTime = time + s
            if now_totalTime < infection_times[a]:
                infection_times[a] = now_totalTime
                heapq.heappush(q,(now_totalTime,a))
    

for t in range(tc):
    INF = int(1e9)
    n, d, c = map(int,input().split())
    graph = [[] for _ in range(n+1)]
    infection_times = [INF] * (n+1)
   
    
    for i in range(d):
        a, b, s = map(int,input().split())
        graph[b].append((a,s))
    dijkstra(c, infection_times, graph)

    cnt,last_time   = 0, 0 # 감염된 컴퓨터 수, 최종 시간
    for i in range(1, n+1):
        if infection_times[i] != INF:
            cnt +=1
            last_time = max(last_time,infection_times[i])
    print(cnt, last_time)