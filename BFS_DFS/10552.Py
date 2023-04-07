# https://www.acmicpc.net/problem/10552 (실버2) DOM
# <DFS recursion>으로 풀었을 경우 시간초과 발생
#
#

import sys
# sys.setrecursionlimit(10**6)
from collections import deque

input = sys.stdin.readline

N, M, P = map(int, input().split())  # N: 사람수, M: 총 채널수 , P: 시작 채널 수
Info = [[] for _ in range(M+1)]
visited = []
Que = deque()

count = 0
Infinite = False  # 무한를 반복하는 것을 체크하는 flag
for i in range(N):
    like, hate = map(int, input().split())
    Info[hate].append(like)
print(Info)
def BFS(v):
    Que.append(v)
    global Infinite, count
    while Que:
        change = Que.popleft()
        count +=1 
        print('cnt',count)
        visited.append(v)
        for i in range(M):
            if Info[change] != 0 and change not in visited:
                Que.append(change)
                break
            elif change in visited:
                Infinite = True


BFS(P)

if Infinite == False:
    print(count)
else:
    print(-1)
            


# 시간초과 발생
# # recursion DFS

# def DFS(v):
#     global count, Infinite
#     if v not in visited:
#         visited.add(v)
#         for i in range(N):
#             if Info[i][0] == v:
#                 count += 1
#                 DFS(Info[i][1])
#                 break

#     else:
#         Infinite = True
# DFS(P)

# if Infinite == False:
#     print(count)
# else:
#     print(-1)
