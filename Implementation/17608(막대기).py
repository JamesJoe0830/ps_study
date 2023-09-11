import sys
# https://www.acmicpc.net/problem/17608
# 17608. 막대기 [🥉 브론즈 2]
# 📚 알고리즘 분류: 구현
# ⏰ 걸린 시간 : 2분
# 
# [문제풀이]
# 0. 막대에 대한 입력을 받고 오른쪽에서 바라보는것이기 때문에 N-1부터 0까지 거꾸로 탐색한다.
# 1. 막대의 길이가 기준보다 클 경우에만 세주고 기준을 다시 바꿔준다.
# 
# ----------------------------------------

input = sys.stdin.readline
N = int(input())
polls = [int(input()) for _ in range(N)]
cnt = 1
base = polls[-1]

for i in range(N-1,-1,-1):
    if base < polls[i]:
        base = polls[i]
        cnt +=1
print(cnt)
# ----------------------------------------
    
