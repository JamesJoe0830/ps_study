# https://www.acmicpc.net/problem/2667
# 2667. 단지번호붙이기 [🥈 실버 1] -> ✨ BFS로 풀어볼 것
# 📚 알고리즘 분류: BFS&DFS
# ⏰ 걸린 시간 : 20분
# 시간복잡도 : O(N^2)
# 
# [문제 접근 방법]
# 0. 한번 DFS로 들어가서 계속 돌면서 cnt 를 올려주고 나오면서 cnt를 return하면
# 0-1. 하나의 단지안에 집의 개수를 탐색할 수 있다.
# 1. hometown에 하나의 단지를 돌고 나와서 집의 개수를 넣어준다.
# 2. 방문한 곳은 0으로 바꿔주면서 다시 재방문하지 않도록 만든다 -> visited 처리
# 
# [recursion DFS 알고리즘 푼 근거 및 회고] 😡 푼 근거가 부족하다. 시간복잡도로 접근해보자
# 0. 한번 탐색시작해서 계속해서 한 단지라면 재귀적으로 탐색하도록 하면 접근하기 쉽다!
# 
# ---------------------------------------------------
import sys
# 그래프의 크기
N = int(input())
graph = []
for i in range(N):
    row_string = input()
    row = [int(ele) for ele in row_string]
    graph.append(row)
hometown = []

# recursion DFS
def DFS(y, x):
    global cnt
    cnt += 1
    graph[y][x] = 0 # visited 처리
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N:
            if graph[ny][nx] == 1:
                DFS(ny, nx)
    return cnt


for y in range(N):
    for x in range(N):
        if graph[y][x] == 1:
            cnt = 0
            hometown.append(DFS(y, x))
print(len(hometown))
hometown.sort()
for complex in hometown:
    print(complex)
# ---------------------------------------------------