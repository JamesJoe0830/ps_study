# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
# N이 격자 모양의 미로
from collections import deque
N, K = map(int,input().split())
moveList = deque(input())
graph = []
move ={
"U" : [0,1],
"D" : [0,-1],
"L": [-1,0],
"R" : [1,0]
}
def check(x,y):
	distance = 0 
	while moveList:
		if x<0 or y<0 or x>=N or y>=N or graph[x][y] == 1 or graph[x][y] ==2:
			continue
			# print('FAIL')
			# break
		next_move = moveList.popleft()
		if next_move == 'U':
			y = y+1
		elif next_move == 'D':
			y = y-1
		elif next_move == 'L':
			x = x-1
		else:
			x = x+1
		distance +=1
		
		
	if graph[x][y] == 2:
		print('SUCCESS', distance)
	

for i in range(N):
	row = list(map(int,input().split()))
	graph.append(row)
	for s in row:
		if s == 1:
			check(i,s)		

# ----------------------------------------------------------------------------------------------------------------------
N, K = map(int, input().split(" "))
queries = input()
board = [list(map(int, input().split(" "))) for _ in range(N)]

def search_start(N, board):
	for row in range(N):
		for col in range(N):
			if board[row][col] == 1:
				return row, col

def solution(N, K, queries , board):
	start_y, start_x = search_start(N, board)
	move = {
		"U" : [-1, 0],
		"D" : [1, 0],
		"L" : [0, -1],
		"R" : [0, 1]
	}
	y, x, count = start_y, start_x, 0
	for query in queries:
		ny = y + move[query][0]
		nx = x + move[query][1]
		if 0<=ny<N and 0<=nx<N and board[ny][nx] != 3:
			y, x, count = ny, nx, count+1
			if board[ny][nx] == 2:
				print(f'SUCCESS {count}')
				return
	
	print("FAIL")
	return


solution(N,K,queries, board)

# ----------------------------------------------------------------------------------------------------------------------
# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
m, n = map(int,input().split())


command = input()

graph = []
for i in range(m):
   graph.append(list(map(int,input().split())))
   
start = [0,0]
end = [0,0]
for i in range(m):
   for j in range(m):
      flag = graph[i][j] 
      if flag == 1:
         start = [i,j]
      if flag == 2:
         end = [i,j]
      

isEnd = False
count = 0
answer = 0
dx = [1,0,-1,0]
dy = [0,1,0,-1]
commands = ['D', 'R', 'U', 'L']

x,y = start[0], start[1]
for i in range(len(command)):
   
   for j in range(4):
      if command[i] == commands[j]:

         new_dx, new_dy = x + dx[j], y + dy[j]
         
         if new_dx < m and new_dx >= 0 and new_dy < m and new_dy >= 0 and graph[new_dx][new_dy] !=3:
            x,y = new_dx, new_dy
            count+=1
            if graph[new_dx][new_dy] == 2:
               isEnd = True
               break
   else:
      continue
   break

if isEnd:
   print("SUCCESS", count)
else:
   print("FAIL")