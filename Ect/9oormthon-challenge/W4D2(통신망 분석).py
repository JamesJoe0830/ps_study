# https://level.goorm.io/exam/195699/%EA%B7%B8%EB%9E%98%ED%94%84%EC%9D%98-%EB%B0%80%EC%A7%91%EB%8F%84/quiz/1
import sys
from collections import deque
input = sys.stdin.readline

# N: 컴퓨터 개수, M: 회선의 개수
N, M = map(int,input().split())
graph = [[] for _ in range(N+1)]
vertex = [[] for _ in range(N+1)]
for i in range(M):
    a, b = map(int,input().split())
    vertex[a].append(b)
    graph[a].append(b)
    graph[b].append(a)

answer = []
Q = deque()
def BFS(node):
    cnt= 0
    Q.append(node)
    visited.add(node)
    visit_now.append(node)
    cnt+=len(vertex[node])
    while Q:
        current = Q.popleft()
        for next_node in graph[current]:
            if next_node not in visited:
               Q.append(next_node)
               visited.add(next_node)
               visit_now.append(next_node)
               cnt+=len(vertex[next_node])
    visit_now.sort()
    answer.append((cnt/len(visit_now),list(visit_now)))
    visit_now.clear()

visited = set()
visit_now = []
for i in range(1,N+1):
    if graph[i] and i not in visited:
        BFS(i)
#출력
answer.sort( key=lambda x:(-x[0], x[1]))

print(*answer[0][1])


