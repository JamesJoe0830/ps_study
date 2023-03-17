# https://www.acmicpc.net/problem/2170 (골드 5)선 긋기-> 오답필요
# <풀이방법>
# 0. 겹치지 않았을때와 겹칠때 나누고
# 1. 시작과 끝지점 계속 변경
import sys
input=sys.stdin.readline
N = int(input())
lines =list()
for _ in range(N):
    lines.append(tuple(map(int,input().split()))) # tuple이 iteration도는게 더 빠름
lines.sort()
start= lines[0][0]
end = lines[0][1]
answer =0
for i in range(1,N):
    if start <= lines[i][0] <= end:
        if end < lines[i][1]:
            end = lines[i][1]
    
    elif end < lines[i][0]: #겹치지 않을때 start end 바꿔주기
        answer += abs(end-start)
        start = lines[i][0]
        end = lines[i][1]
answer += abs(end-start) # 마지막에 나왔을때 시작과 끝을 더해줘야한다.
print(answer)