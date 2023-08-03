# https://www.acmicpc.net/problem/11657
# 11657. 타임머신 [🥇 골드 4] -> 🔥 오답 필요
# 📚 알고리즘 분류: 벨만 포드 
# ⏰ 걸린 시간 : 시간초과 (벨만 포드 알고리즘으로 처음)
# 시간복잡도 : O(VE)
# 
# [벨만 포드 알고리즘 푼 근거 및 회고]
#  0. 음의 가중치를 사용한다. 
#  1. 음의 가중치만 있을 경우에는 다익스트라로 풀 수 있지만,
#  2. 음의 사이클이 발생하는 문제는 음의 사이클을 체크할 수 있는 벨만포드로 풀어야한다.
# 
# ✔️ 벨만 포드 전제 조건
# 0. 최단 경로는 사이클을 포함할 수 없기 때문에, 최대 V-1개의 간선만 사용할 수 있다.
# ------------------------------------------------
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
INF = int(1e9)
distance = [INF]*(N+1)
graph = [[] for _ in range(N+1)]
negative_cycle = False
for _ in range(M):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))

def bellman(start):
    global negative_cycle
    distance[start] = 0

    for i in range(1,N+1): #간선을 탐색하는 for문 간선이 n-1개여야 사이클이 발생하지 않는다.
        for a in range(1,N+1): #node 탐색하는 for문 
            for next, time in graph[a]:
                if distance[a] != INF and distance[next] > distance[a] + time:
                    distance[next] = distance[a] + time
                    if i == N: #n-1번 이후에도 값이 갱신되면 음수 사이클 존재.
                        negative_cycle = True
                        break
    return negative_cycle

bellman(1)

# 출력
if negative_cycle == True:
    print(-1)
else:
    for i in range(2,N+1):
        if distance[i] == INF:
            print(-1)
        else:
            print(distance[i])