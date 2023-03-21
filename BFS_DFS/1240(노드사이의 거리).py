# https://www.acmicpc.net/problem/1240 (골드 5) => 오답 필요
# <BFS 근거>
# 0. recursion DFS 는 없다면 distance 를 이전단계로 해줄 수 있는 코드 작성이 복잡
# 1. 해당 노드의 최적의 거리
# <주의 사항>
# 0. 가장 최적의 거리 측정
# 0. 노드와 거리를 동시에 넣고 pop할 것

import sys
input = sys.stdin.readline
from collections import deque
N, M = map(int, input().split())
graph = [[0]*(N+1) for _ in range(N+1)]
visited = list()
answer = list()

for _ in range(N-1):
    a, b, l = map(int, input().split())
    graph[a][b] = l
    graph[b][a] = l

# BFS 
def BFS(start,des): # des: destination
    Que.append((start,0))
    visited.append(start)
    while Que:
        n, d = Que.popleft() # n: 노드 d: distance

        if n == des: # 목적지와 노드가 일치하면 정답 배열에 저장후 종료
            answer.append(d)
            return
        for i in range(N+1):
            if graph[n][i] != 0 and i not in visited:
                visited.append(i)
                Que.append((i,d+graph[n][i]))

for _ in range(M):
    x, y =map(int,input().split())
    visited =[] # 다시 들어갈때 방문 배열 초기화
    Que = deque() # Que 초기화
    BFS(x,y)

for _ in range(len(answer)):
    print(answer[_])







# # recursion DFS -> 방문한 노드의 가중치 값을 계산하는 것이 불편함
# def DFS(X,y): # 1 2 받아옴
#     visited.append(X)
#     global answer
#     if X == y :
#         anslist.append(answer)
#         return
#     for i in range(N+1):
#         if graph[X][i] != 0 and i not in visited:
#             visited.append(i)
#             answer += graph[X][i]
#             DFS(i,y)
    
    

# for i in range(M):
#     x, y =map(int,input().split())
#     answer=0 # answer = 0으로 선언 및 초기화
#     visited =[] # 다시 Recursion 들어갈때 방문 배열 초기화
#     DFS(x,y)

# for i in range(len(anslist)):
#     print(anslist[i])


