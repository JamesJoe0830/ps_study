# https://www.acmicpc.net/problem/1374(골드 5) -> 오답필요, 아이디어 생각 안남
# <Greedy>
# <주의 사항>


import sys
input = sys.stdin.readline

N = int(input())
Class = [[0] for _ in range(N+1)]
overlap = []
overlap.append(0)
count = 0
for _ in range(N):
    num, s, e = map(int,input().split())
    Class[num] = [str, e]
Class.sort()
print(Class)


for i in range(1,N+1):
    count=0
    start = Class[i][0]
    end = Class[i][1]
    for j in range(i,N+1):
        if end <= Class[i][0]:
            count +=1 
            overlap.append(count)
