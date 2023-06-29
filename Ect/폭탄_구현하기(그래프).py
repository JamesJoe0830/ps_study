# 폭탄 구현하기
N, K = map(int,input().split())
graph = [[0]* N for i in range(N)]

#check 함수 
def Check(x,y):
	dx = [0,0,-1,1]
	dy = [-1,1,0,0]
	graph[x][y] += 1
	for i in range(4):
		x1 = x + dx[i]
		y1 = y + dy[i]
		if 0<= x1 <N and 0<= y1 <N:
			graph[x1][y1] += 1


for i in range(K):
	a, b = map(int,input().split())
	Check(a-1,b-1)

#출력
answer = 0
for i in range(N):
	for j in range(N):
		answer += graph[i][j]
print(answer)	
