# https://www.acmicpc.net/problem/1865
# 1865. 웜홀 [🥇 골드 3] -> 🔥 오답 필요 [오답 횟수: 1회]
# 📚 알고리즘 분류: 벨만 포드 
# ⏰ 걸린 시간 : 42분 
# 시간복잡도 : O(VE)
# 
# [벨만 포드 알고리즘 푼 근거 및 회고]
#  0. 음의 가중치를 사용한다. 
#  1. 음의 가중치만 있을 경우에는 다익스트라로 풀 수 있지만,
#  2. 음의 사이클이 발생하는 문제는 음의 사이클을 체크할 수 있는 벨만포드로 풀어야한다.
# 
# ✔️ [벨만 포드 전제 조건]
# 0. 최단 경로는 사이클을 포함할 수 없기 때문에, 최대 V-1개의 간선만 사용할 수 있다.
# 1. 그래야 사이클이 발생하지 않는다!
#
# 💡[출발을 하였을 때보다 시간이 되돌아가 있는 경우가 있는지] 
#  -> 음의 사이클이 발생하면 생긴다!
# ------------------------------------------------------------
import sys
input = sys.stdin.readline

TC = int(input())
# N: 지점의 수, M: 도로의 개수, W: 웜홀의 개수
for t in range(TC):
    N ,M ,W = map(int,input().split())
    INF = int(1e9)
    times = [INF] * (N+1)
    roads = [[] for _ in range(N+1)]

    for i in range(M):
        #S: 시작점, E: 도착 지점, T: 줄어드는 시간
        S, E, T = map(int,input().split())
        roads[S].append((E,T))
        roads[E].append((S,T))
    for i in range(W):
        S, E, T = map(int,input().split())
        roads[S].append((E,-T))

    def bellman(start):
        times[start] = 0

        for i in range(1,N+1):
            for S in range(1,N+1):
                for E, T in roads[S]:
                    if times[E] > times[start]+T: 
                        # 여기서 INF != times[S] 를 하지 않는 이유: 모든 노드에서 시작하지 않고 1번에서만 검사를 할때 1-2-3 4-5 이런식으로 끊긴 노드가 발생하면 4-5를 검사하지 못하기 때문
                        times[E] = times[start]+T
                        if i == N: #N번 이후에도 값이 갱신되면 음수 사이클 존재.
                            return print('YES')
        return print('NO')

    bellman(1)

