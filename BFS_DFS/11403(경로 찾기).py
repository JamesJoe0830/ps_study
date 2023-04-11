# https://www.acmicpc.net/problem/11403 -> 경로 찾기 (실버1) 플로이드 워셜
# Recursion DFS
# <주의할 점 및 포인트>
# 사이클 인지 확인 어떻게 할 것인가 ?


# <풀이방법 1번> 
# ----------------------------------------------------------------------------
# [Recursion DFS] 사용
# -> 0번에 비해서 되게 간단하고 한줄을 대상으로 비교하는 것
# 싸이클에 대해 시간초과 및 메모리초과를 해결할 수 있는 좋은 방법 !
import sys
input = sys.stdin.readline

N = int(input())
graph = [list(map(int,input().split())) for _ in range(N)]

# recursion DFS
def DFS(v):
    for x in range(N):
        if ans_graph[x] == 0 and graph[v][x] == 1:
            ans_graph[x] = 1
            DFS(x)

for i in range(N):
    # 한줄만 생성하면서 그때마다 출력하는게 가능하다.
    ans_graph = [0 for _ in range(N)] # 한줄에 대해서 싸이클 다 확인하기 
    DFS(i)
    print(*ans_graph) 
# ----------------------------------------------------------------------------


# <풀이방법 2번> -> 오답시 다시 볼 것
# ----------------------------------------------------------------------------
# [플로이드 워셜]
# 모든정점에 대해서 탐색하는 플로이드 워셜
# import sys
# # input = sys.stdin.readline
# N = int(input())
# graph = [list(map(int,input().split())) for _ in range(N)]
# for i in range(N):
#     for j in range(N):
#         for k in range(N):
#             if graph[i][j] == 1 and graph[i][k] == 1:
#                 graph[j][k] = 1





# ----------------------------------------------------------------------------



# <풀이방법 0번 > DFS recursion 메모리초과 / 시간초과 발생 -> 문제 해결 어떻게 해야할지 고민
# Recursion DFS 사용

# ----------------------------------------------------------------------------
# import sys
# sys.setrecursionlimit(10**6)
# input = sys.stdin.readline

# N = int(input())
# graph = [list(map(int,input().split())) for _ in range(N)]
# ans_graph = [[0]*N for _ in range(N)]

# # recursion DFS
# def DFS(start,end):
#     ans_graph[start][end] = 1
#     visited.append((start,end))
#     for i in range(N):
#         if graph[end][i] == 1 and (end,i) not in visited:
#             DFS(start,i)


# for i in range(N):
#     visited = [] # 이게 핵심 결국에 계속 visited를 초기화해줘서 싸이클 돌 수 있도록
#     for j in range(N):
#         if graph[i][j] == 1 and (i,j) not in visited:
#             DFS(i,j)

# # 출력을 위한 것
# for row in ans_graph:
#     print(*row)
# -----------------------------------------------------------------------------