# https://www.acmicpc.net/problem/3020
# 3020. 개똥벌레 [🥇 골드 5] 
# 📚 알고리즘 분류: 구간 합
# ⏰ 걸린 시간 : 68분 
# 
# 
# 🍯 포인트 : 어떻게 높이들을 모두 누적해서 담을 것인가? [ 7, 8, 10, 8, 7] 
# 0. 위에서 자라는 것과 아래에서 자라는 것을 따로 저장한다.
# 1. 닿는 위치를 저장한다.
# 2-1.아래에서 자라는 것은 위에서 부터 누적합쓰고
# 2-2.위에서 자라는 것은 아래에서 부터 누적합을 쓰고
# 3. 결국 이 둘을 더하게 되면 높이가 된다.
#
# 
# [구간 합 알고리즘 푼 근거 및 회고]
#  0. 구간합을 쓰지않고 바로 for 문으로 결과를 탐색하게 하면 시간초과가 발생한다. 20만 50만 입력값이므로
# ---------------------------------------------------------------------------------------

import sys
input = sys.stdin.readline
# N : 동굴의 길이 H: 동굴의 높이
N, H = map(int,input().split())
heights = [0]*(H+1)
flag = True
bottom = [0]*(H+1) #아래서 자라는놈 
top = [0]*(H+1) # 위에서 자라는놈 
for i in range(N):
    a= int(input())
    if flag== True:
        bottom[a] +=1
        flag=False
    else:
        top[H+1-a] +=1
        flag=True

start=False
for i in range(H-1,0,-1):
    bottom[i] +=bottom[i+1]
for i in range(1,H+1):
    if top[i] !=0: 
        start=True
    if start:
        top[i] +=top [i-1]
for i in range(H+1):
    heights[i]= bottom[i]+top[i]
heights.pop(0)

mini=min(heights)
count=heights.count(mini)

print(mini, count)
    
    
# ---------------------------------------------------------------------------------------
