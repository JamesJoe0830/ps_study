# https://www.acmicpc.net/problem/1012 (유기농 배추) 실버2

import sys
sys.setrecursionlimit(10000) #재귀 한도를 1000까지 풀어줌 (파이썬에서 재귀 한도가 시스템안정을 위해서 정해져있기 때문에)

def DFS(x,y):
    if x<0 or x>=N or y<0 or y>=M: # graph범위 넘어가면 재귀함수 종료
        return False    
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    if graph[x][y] == 1 and visited[x][y] == 0:
        visited[x][y] =1
        for i in range(4):
            X1 = x + dx[i]
            Y1 = y + dy[i]
            DFS(X1,Y1)
answer= []
T = int(sys.stdin.readline())

for t in range(T):
    M, N, K = map(int, sys.stdin.readline().split()) #M은 가로 N은 세로
    graph = [[0]*(M) for i in range(N)] 
    visited = [[0]*(M) for i in range(N)]
    count = 0
    for i in range(K):
        X, Y = map(int, sys.stdin.readline().split())
        graph[Y][X] =1
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1 and visited[i][j] == 0:
                DFS(i,j)  
                count +=1 
    answer.append(count)

for i in answer:
    print(i)
