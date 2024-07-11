# https://www.acmicpc.net/problem/2668
# 사이클을 구성하는 부분 노드의 개수를 세는 문제

import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(10**6))

N = int(input())
numlist = [0]*(N+1) # 3 1 1 5 5 4 6
visited = [0]*(N+1) # 방문 리스트
finished = [0]*(N+1)  # 종점을 체크해주는 리스트
answer = list()

for i in range(N):
    num = int(input())
    numlist[i+1] = num

for j in range(1,N+1): # 왕복이 불가능한 점들 0으로 대체 
    if j not in numlist:
        numlist[j] = 0


def DFS(v):
    visited[v] = 1
    next =numlist[v]
    if visited[next] ==0  and numlist[next] !=0: 
        DFS(next)
    # 방문은 했지만, 사이클이 안된 case
    elif finished[next] ==0:
        while next != v:
            answer.append(next)
            next = numlist[next]
        answer.append(v)
    finished[v] = 1

for i in range(N+1):
    if numlist[i] != 0 and visited[i] == 0:
        DFS(i)


print(len(answer))  # 정답의 개수 추출 
answer.sort()
for i in answer:
    print(i)