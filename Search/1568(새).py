import sys
N = int(sys.stdin.readline())
cnt = 0
i=1
while True:
    if N == 0: # while 끝내는 조건문
        print(cnt)
        break
# 만약, 현재 나무에 앉아있는 새의 수가 지금 불러야 하는 수 보다 작을 때는, 1부터 게임을 다시 시작 
    if N-i>=0: 
        N = N-i
        cnt += 1
    elif N-i<0:
        i =1
        N = N -i
        cnt += 1
    i = i+1