import sys
input=sys.stdin.readline


def check(y, x):
    global cnt
    cnt +=1
    print('cnt',cnt)
    if (y,x) not in visited:
        visited.append((y,x))
        print(y,x)
        print(visited)
        dy = y + board[y][x][0]
        dx = x + board[y][x][1]
        if x != dx:
            nx = x
            for i in range(abs(board[y][x][1])):
                if board[y][x][1] < 0 :
                    nx -= 1
                    if nx < 0:
                        nx = N-1
                        check(y,nx)
                        break
                    else:
                        check(y,nx)
                if board[y][x][1] > 0 :
                    nx += 1
                    if nx >= N :
                        nx = 0
                        check(y,nx)
                        break
                    else:
                        check(y,nx)
        elif y != dy:
            ny = y
            for i in range(abs(board[y][x][0])):
                if board[y][x][0] < 0:
                    ny -= 1
                    if ny < 0:
                        ny = N-1
                        check(ny,x)
                        break
                    else:
                        check(ny,x)
                elif board[y][x][0] > 0:
                    ny += 1 
                    if ny >= N:
                        ny = 0
                        check(ny,x)
                        break
                    else:
                        check(ny,x)
    elif (y,x) in visited:
        if cnt % 2 == 0 :
            answer.append(cnt)
        else: 
            answer.append(cnt-1)
        cnt = 0




N= int(input())
Rg, Cg= map(int,input().split())
Rp, Cp = map(int,input().split())
board = [input().split() for _ in range(N)]
answer = []
for i in range(N):
    for j in range(N):
        if board[i][j][-1] == 'L':
            board[i][j] = (0,-1*int(board[i][j][:-1]))
        elif board[i][j][-1] == 'R':
            board[i][j] = (0,1*int(board[i][j][:-1]))
        elif board[i][j][-1] == 'D':
            board[i][j] = (int(board[i][j][:-1]),0)
        else:
            board[i][j] = (-1*int(board[i][j][:-1]),0)
cnt = 0
visited = [] 
check(Rg-1,Cg-1)
# visited = []
# check(Rp-1,Cp-1)
print(board)
print(answer)


if answer[0]< answer[1]:
    print('player', answer[1])
elif answer[0]> answer[1]:
    print('goorm', answer[0])

