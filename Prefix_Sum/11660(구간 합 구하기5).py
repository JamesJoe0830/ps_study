# https://www.acmicpc.net/problem/11660
# 11660. 구간 합 구하기5 [🥈 실버 1] -> 오답 필요 🔥
# 📚 알고리즘 분류: 구간 합
# ⏰ 걸린 시간 : 시간초과 -> 초기를 [[0]*(N+1)]이렇게 설정해주지 않아서 예외처리 하려다가 시간초과
# 
# [구간 합 알고리즘 푼 근거 및 회고]
#  0. 구간합을 쓰지않고 그때마다 결과를 탐색하게 하면 시간초과가 발생한다.
# 
# 
# 
# ------------------------------------------------------------------------------------------------

import sys
input=sys.stdin.readline
N, M = map(int, input().split())
graph = [[0]* (N+1)]
# print(graph)
for i in range(1,N+1):
    arr =[0]+ list(map(int,input().split()))
    graph.append(arr)

# print(graph)
# 열 누적 
for x in range(1,N+1):
    for y in range(2,N+1):
        graph[x][y] += graph[x][y-1]

# 행 누적 
for x in range(2,N+1):
    for y in range(1,N+1):
        graph[x][y] += graph[x-1][y]
# print(graph)

# [[0, 0, 0, 0, 0], [0, 1, 3, 6, 10], [0, 3, 8, 15, 24], [0, 6, 15, 27, 42], [0, 10, 24, 42, 64]]
for tc in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    print(graph[x2][y2] - graph[x2][y1-1]- graph[x1-1][y2]+graph[x1-1][y1-1])

# -----------------------------------------------------------------------------------------------

# # 가로 더하기
# for y in range(N):
#     row= 0
#     for x in range(N):
#         row+=graph[y][x]
#         prefix_graph[y][x]+=row

# # 세로 더하기 
# for y in range(1,N):
#     column=0
#     for x in range(0,N):
#         prefix_graph[y][x]+=prefix_graph[y-1][x]

# print(prefix_graph)

# for i in range(M):
#     x1, y1, x2, y2 = map(int, input().split())
#     if x1==1 and y1==1 :
#         print(prefix_graph[x2-1][y2-1])
#         continue
#     if x1==x2 and y1==y2 :
#         print(graph[x1-1][y1-1])
#         continue
#     if x1>1 and x2>1 and y1>1 and y2>1 : 
#         print(prefix_graph[x2-1][y2-1]-prefix_graph[x1-2][y2-1]-prefix_graph[x2-1][y1-2]+prefix_graph[y1-2][x1-2])
    

# [1, 3,  6, 10]
# [3, 8,  15, 24], 
# [6, 15, 27, 42],
# [10, 24,42, 64]
# 1 2 3 4
# 3 4 5 6
# 4 5 6 7
# 2 2 3 4


