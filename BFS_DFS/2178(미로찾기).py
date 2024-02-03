# https://www.acmicpc.net/problem/2178
# 2178. 미로 찾기 [🥈 실버 1] 
# 📚 알고리즘 분류: BFS&DFS
# ⏰ 걸린 시간 : 20분
# 시간복잡도 : O(N*M)
# 
# [문제 접근 방법]
# 0. 미로를 찾을때 1인 곳을 탐색한다.
# 1. BFS알고리즘에서 Que를 사용해서 트리의 같은 계층에서 뻗어나간 거리를 각각 저장한다.
# 2. Que에서 빼낼때 현재 있는 곳까지의 거리를 함께 뽑아낸다.
# 3. 목적지에 도달한 경우 해당 거리를 answer 배열에 넣고 
# 4. answer 배열중 제일 작은 값이 최소의 칸의 수이다.
# [주의사항]
# Q에 값을 넣을때 이미 있는 값을 걸러야 한다. -> 하지 않으면 메모리 초과 발생
# [BFS 알고리즘 푼 근거 및 회고]
# 0. 해당 노드로 부터 같은 Layer로 뻗어 나가면서 거리를 측정하기에 적합하기 때문이다.
# 1. DFS의 경우 깊이를 우선 탐색하기 때문에 각각 현재의 거리를 측정해 나가기에 적합하지 않다고 판단함.
# -----------------------------------------------------------------------------
import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int,input().rstrip())) for _ in range(N)]
Q = deque()
answer = []

def BFS(y,x):
    distance = 1
    Q.append((y,x,distance))
    dy = [0,0,-1,1]
    dx = [-1,1,0,0]
    while Q:
        y,x,distance = Q.popleft() 
        graph[y][x] = 0
        if y==N-1 and x==M-1:
            answer.append(distance)
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0<= ny < N and 0<= nx < M and graph[ny][nx] ==1:
                next_distance = distance + 1 
                if (ny,nx,next_distance) not in Q: 
                # 해당 부분이 없으면 메모리 초과가 발생한다.
                    Q.append((ny,nx,next_distance))
    print(min(answer))

BFS(0,0)

# -----------------------------------------------------------------------------