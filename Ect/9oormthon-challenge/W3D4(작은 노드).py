# https://level.goorm.io/exam/195696/%EC%9E%91%EC%9D%80-%EB%85%B8%EB%93%9C/quiz/1
import sys
from collections import deque

input = sys.stdin.readline
N, M, K = map(int, input().split())
nodes = [[] for i in range(N+1)]
visited = set()
for i in range(M):
    s, e = map(int, input().split())
    nodes[s].append(e)
    nodes[e].append(s)
# print(nodes)
Q = deque()
def BFS(s):
    Q.append(s)
    visited.add(s)
    while Q:
        s = Q.popleft()
        nodes[s].sort()
        for e in nodes[s]:
            if e not in visited:
                Q.append(e)
                visited.add(e)
                break

    return print(len(visited), s)
BFS(K)
