import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline
N=int(input())
graph = [list(input().rstrip()) for _ in range(N)]
visited = [[0]*N for _ in range(N)] # 방문한곳을 체크하는 리스트
dx =[-1,1,0,0]
dy =[0,0,-1,1]


#recursion DFS
def DFS(x,y):
    color=graph[x][y] #색이 같은 경우를 따져주기 위함
    visited[x][y] = 1

    for i in range(4):
         nx = x + dx[i]
         ny = y + dy[i]
         if 0 <= nx <= N -1 and 0 <= ny <= N-1 and visited[nx][ny] ==0: # 이 조건을 통해 recursion 끝남
            if color ==graph[nx][ny]:
                DFS(nx,ny)
    

# R,G,B 적록색약이 없는 경우
count_common = 0 # 일반인의 경우 세는 변수
for i in range(N):
    for j in range(N):
        if visited[i][j] ==0:
            DFS(i,j)
            count_common +=1

# R,G,B적록색약이 있는 경우
for i in range(N):
    for j in range(N):
        if graph[i][j] =='G': # Green을 Red로 바꿔줌
            graph[i][j] ='R'
visited = [[0]*N for _ in range(N)]
count_uncommon =0
for i in range(N):
    for j in range(N):
        if visited[i][j]==0:
            DFS(i,j)
            count_uncommon +=1
print(count_common,count_uncommon)


        