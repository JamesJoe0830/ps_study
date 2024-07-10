import sys
N = int(sys.stdin.readline())
visit = [[0]*N for i in range(N)]
graph = [[0]*N for i in range(N)] # 입력을 받아온거임
for i in range(N):
    a = sys.stdin.readline()
    for j in range(N):
        graph[i][j] = int(a[j])
###########################################
count =0
apartment_complex = 0
# print('g',graph) 
def dfs(x, y) :
    global count
    if x<0 or x>=N or y<0 or y>=N:
        return False
    dx =[-1,1,0,0]
    dy =[0,0,-1,1]
   
    if graph [x][y] == 1 and visit[x][y] == 0:
        count +=1
        visit[x][y]=1
        for i in range(4):
            x2 = x+dx[i]
            y2 = y+dy[i]
            dfs(x2,y2)

for i in range(N):
    for j in range(N):
        if graph[i][j] ==1 and visit[i][j] == 0:
            apartment_complex +=1
            dfs(i,j)
            print(count)
            count=0
print(apartment_complex)
            

            
