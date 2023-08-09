# https://www.acmicpc.net/problem/1446
# 1446. 지름길 [🥈 실버 1] -> 🔥 오답 필요 [오답 횟수: 1회]
# 📚 알고리즘 분류: 다익스트라 알고리즘
# ⏰ 걸린 시간 : 시간초과 (다익스트라 알고리즘으로 처음 풀어봐서 어려움)
# 시간복잡도 : 다익스트라 -> O(ElogV) : EV인데 우선순위 큐 사용해주면 탐색이 logV로 줄어든다.
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
import heapq # 우선순위 큐 라이브러리 O(logN)
import sys
input = sys.stdin.readline

INF = int(1e9) #무한을 의미하는 값으로 10억을 설정

# N:지름길의 개수, D:고속도로 길이
N, D = map(int,input().split())
graph = [[] for _ in range(D+1)]
# 최단 거리를 일단 무한으로 초기화
distance = [INF] * (D+1)
# 일단 거리를 1로 초기화
for i in range(D):
    graph[i].append((i+1, 1))

# 지름길이 있으면 업데이트
for _ in range(N):
    start, end, length = map(int,input().split())
    if end > D : #만일 고속도로 길이보다 end값이 크면 무시
        continue
    graph[start].append((end,length))
    # start에 end와 length값 넣어주기

# 다익스트라 정의    
def dijkstra(start):
    Que=[]
    heapq.heappush(Que,(0,start))  #start노드로 가기 위한 최단경로를 0으로 설정하여 큐에 삽입
    distance[start]=0
    while Que:
        dist, now = heapq.heappop(Que)  # dist는 여태까지 거리

        if dist > distance[now]:
            continue
        for i in graph[now]:
            now_dist= dist +i[1]
            if now_dist < distance[i[0]]:  # 현재거리 < end값 (즉, 지름길을 택했을 때가 더 짧은 경우)
                distance[i[0]] = now_dist # 거리를 지름길로 대체함
                heapq.heappush(Que,(now_dist, i[0])) #(현재까지거리, 현재시점)



# print(graph)

dijkstra(0)
print(distance[D])
# ------------------------------------------------------------
