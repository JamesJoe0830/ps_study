# https://www.acmicpc.net/problem/1449 -> 수리공 항승(실버 3) -> greedy (오답필요)
# start를 활용한 좋은문제 start를 계속해서 업데이트 해줌

# <Greedy인 이유>
# 0. 테이프의 최소 개수를 구하는 문제

# <문제 접근>
# 0.
# 
# --------------------------------------------------------------------------

import sys
input = sys.stdin.readline

N, L = map(int,input().split())
leaks = list(map(int,input().split()))
leaks.sort()
start = leaks[0]
cnt = 1
for i in range(N):
    if leaks[i] >= start +L:
        cnt+=1 # 길이 초과하면 새 테이프 붙임
        start = leaks[i]
print(cnt)




# 틀린 코드---------------------------------------------------------------------

# cnt = N
# i = 0

# while True:
#     if i > N-2:
#         print(cnt)
#         break
#     if i < N-2:
#         for j in range(i+1,N-1):
#             if leaks[j] - leaks[i] +1 <= L < leaks[j+1] -leaks[i] +1:
#                 cnt = cnt - (j-i)
#                 i = j
#                 break
#     elif i == N-2:
#         if leaks[N-1] - leaks[N-2] + 1 <= L:
#             cnt -= 1
#     i += 1
# --------------------------------------------------------------------------





