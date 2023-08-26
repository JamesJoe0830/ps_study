# https://level.goorm.io/exam/195691/%ED%8F%AD%ED%83%84-%EA%B5%AC%ED%98%84%ED%95%98%EA%B8%B0-2/quiz/1

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
graph = [input().split() for _ in range(N)]
bombs = [[0]*N for _ in range(N)]
dx = [0, 1, -1, 0, 0]
dy = [0, 0, 0, 1, -1]

def check(y, x):

    for i in range(5):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N:
            if graph[ny][nx] == "@":
                bombs[ny][nx] += 2
            elif graph[ny][nx] == "#":
                bombs[ny][nx] += 0
            else:
                bombs[ny][nx] += 1

for i in range(K):
    y, x = map(int, input().split())
    check(y-1, x-1)

max_value = -1
for line in bombs:
    if max(line) > max_value:
        max_value = max(line)
print(max_value)
