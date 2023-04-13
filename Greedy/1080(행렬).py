# https://www.acmicpc.net/problem/1080 -> 행렬 (실버 1) -> 오답필요
# 이게 왜 BFS / DFS 로 안풀지 ? -> 오답시 접근해보자
# <풀이방법>
# 0. 바꾸는 함수 필요 / 마지막에 graph 함수와 answer graph 체크하는 이중 for문 필요
# 1. 
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

graph = [list(map(int,input().rstrip())) for _ in range(N)]
ans_graph = [list(map(int,input().rstrip())) for _ in range(N)]

count = 0 
#바꾸는 함수 호출 -> 이거 필요 없는거 아니야 ? 밑에꺼 풀면??
def check():
    for i in range(N):
        for j in range(M):
            if graph[i][j] != ans_graph[i][j]:
                return False
    return True 

def change(x,y):
    for i in range(x,x+3):
        for j in range(y,y+3):
            if graph[i][j] == 1:
                graph[i][j] = 0
            elif graph[i][j] == 0:
                graph[i][j] = 1

# if 0< N <3 or 0<M<3:  # 이거 넣으면 틀림 -> 왜틀리지 ?
#     print(-1)
# else :
    # 왼쪽 상단 체크하면서 볼 것이기 때문에 (오답할때 보자)
for i in range(0,N-2):
    for j in range(0,M-2):
        if graph[i][j] != ans_graph[i][j]:
            count +=1
            change(i,j)
if check():
    print(count)
else:
    print(-1)