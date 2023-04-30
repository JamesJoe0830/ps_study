# https://www.acmicpc.net/problem/5567 (결혼식)

import sys
input =sys.stdin.readline
from collections import deque
n= int(input())
m= int(input())
friends = [[0]*(n+1) for _ in range(n+1)]
invite = []

for i in range(m):
    a, b = map(int,input().split())
    friends[a][b]=1
    friends[b][a]=1

def BFS(v):
    Que = deque([v])
    for i in range(n+1):
        if friends[v][i] ==1:
            Que.append(i) #여기서 친구만 큐에 넣어주므로 더 안내려감 
            invite.append(i)
    if not invite:
        print(0)
    else:
        while True:
            if not Que:
                return print(len(invite)-1)
                
            t=Que.popleft()
            for i in range(n+1):
                if friends[t][i]==1 and i not in invite:
                    invite.append(i)
BFS(1)