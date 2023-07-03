# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
# 위에서 i번째 왼쪽에서 j 번쨰 (i,j)
N = int(input())
graph = list(list(map(int,input())) for i in range(N))
answer = list([0]*N for i in range(N))

# check
def check(start_x,start_y,x,y,mins):
	while True:
		#아래로만 하강
		if y < N:
			if graph[x][y] ==1 and abs(start_y-y)!=0:
				mins.append(abs(start_y-y))
				y = start_y
				break
		else:
				y = start_y
				break 
		y+=1
	while True:
		#위로만 상승:
		if y >= 0:
			if graph[x][y] ==1 and abs(start_y-y)!=0:
				mins.append(abs(start_y-y))
				y = start_y
				break
		else:
				y = start_y
				break
		y -=1
	while True:
		#왼쪽쪽으로만 상승:
		if x >= 0:
			if graph[x][y] ==1 and abs(start_x-x)!=0:
				mins.append(abs(start_x-x))
				x = start_x
				break
			
		else:
				x = start_x
				break
		x -=1
	while True:
		#오른쪽으로만 상승:
		
		if x < N:
			if graph[x][y] ==1 and abs(start_x-x)!=0:
				mins.append(abs(start_x-x))
				x = start_x
				break
		else:
				x = start_x
				break
		x +=1
	if mins :
		answer[start_x][start_y] = min(mins)
	else:
		answer[start_x][start_y] = -1


for i in range(N):
	for j in range(N):
		mins=[]
		if graph[i][j] == 1:
			answer[i][j] = 0
		else:
			check(i,j,i,j,mins)
#출력
for i in range(N):
	print(*answer[i])
# [준서 코드]--------------------------------------------------------------
from collections import deque

N = int(input())
board = [list(map(int, list(input()))) for _ in range(N)]

def bfs(start_y, start_x, board, result, N):
	if board[start_y][start_x] == 1:
		result[start_y][start_x] = 0
		return
	
	queue = deque([(start_y, start_x, 0,[-1,1,0,0],[0,0,-1,1])])
	while queue:
		y, x, count, dy, dx = queue.popleft()
		for i in range(len(dy)):
			ny = y + dy[i]
			nx = x + dx[i]
			n_count = count + 1
			
			if 0 <= ny < N and 0 <= nx < N:
				queue.append((ny, nx, n_count, [dy[i]], [dx[i]]))
				if board[ny][nx] == 1:
					result[start_y][start_x] = n_count
					return

	result[start_y][start_x] = -1
	return

def solution(N, board):
	result = [[0] * N for _ in range(N)]
	answer = ""
	for row in range(N):
		for col in range(N):
			bfs(row, col, board, result, N)
			
	for row in range(N):
		for col in range(N):
				answer += f'{result[row][col]} '
		answer += "\n"
	print(answer)
	return

solution(N, board)
# [준서 코드]--------------------------------------------------------------
# [준규님 코드]--------------------------------------------------------------
# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

# 0일 경우 상하좌우로만 bfs한다고 생각하면 될듯
# 1을 찾으면 멈춤 해당값 answer에 저장
# 1일 경우 answer에 0 으로 저장
# 1을 못찾고 끝날 경우 -1로 넣으면됨 
from collections import deque
n = int(input())

graph = []
for i in range(n):
   s = input()
   tmp = []
   for j in s:
      tmp.append(int(j))
   graph.append(tmp)


   
answer = [[0 for i in range(n)] for j in range(n)] 

commands = ['D', 'R', 'U', 'L']
dx = [1,0,-1,0]
dy = [0,1,0,-1]

for i in range(n):
   for j in range(n):
      start = [i, j]
      
      if graph[i][j] == 1:
         answer[i][j] = 0
         continue
         
         
      # i, j에서 bfs를 실행하는데, 특정 조건이 필요함 ㅇㅇ
      q = deque()
      q.append(start)
      
      start_flag = False
      continue_flag = False
      while q:
         c = q.popleft()
         # start 부터 처리해야함
         if len(c) == 2:
            
            for k in range(4):
               new_dx, new_dy = c[0] + dx[k], c[1] + dy[k]
               
               # [i, j, 'U'] 이런 형식으로 넣어줘야함
               if new_dx >= 0 and new_dx < n and new_dy >= 0 and new_dy < n:
                  
                  if graph[new_dx][new_dy] == 1:
                     answer[c[0]][c[1]] = 1
                     start_flag = True
                  else:
                     # count 값임
                     tmp = [c[0], c[1], commands[k], 1]
                     q.append(tmp)
            continue
         if start_flag:
            break
            
         elif start_flag == False: # start 이외의 경우 ,q 에는 지금 상하좌우 값들이 들어가있음

            command = c[2]
            
            for k in range(4):
               if commands[k] == command:
                  new_dx, new_dy = c[0] + dx[k], c[1] + dy[k]
                  if new_dx >= 0 and new_dx < n and new_dy >= 0 and new_dy < n:
                  
                  
                     if graph[new_dx][new_dy] == 1:
                        answer[i][j] = c[3]
                        continue_flag = True

                     elif graph[new_dx][new_dy] == 0:
                        q.append([new_dx, new_dy, command, c[3] + 1])
         
         if continue_flag:
            break
      else:
         answer[i][j] = -1
            
         
      
for i in range(n):
   for j in range(n):
      print(answer[i][j], end = ' ')
      
   print()
# [준규님 코드]--------------------------------------------------------------