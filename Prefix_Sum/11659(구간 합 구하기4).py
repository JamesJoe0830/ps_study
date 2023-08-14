# https://www.acmicpc.net/problem/11659
# 
# 걸린 시간 : 20분 
# 
# [문제 접근 방법 및 후기]
# 구간 합을 먼저 구해놓는게 관건이다. 
# N^2으로 구해버리면 시간초과가 발생하기 때문이다.
# 
# ------------------------------------------------------------
import sys
input=sys.stdin.readline
N, M = map(int, input().split())
nums = list(map(int,input().split()))
prefix_sum = []

psum=0
for i in nums:
    psum += i
    prefix_sum.append(psum)


for i in range(M):
    start, end = map(int,input().split())
    if start != 1:
        print(prefix_sum[end-1]-prefix_sum[start-2])
    else: 
        print(prefix_sum[end-1])

# ------------------------------------------------------------
# [시간 초과 코드]
# import sys
# input=sys.stdin.readline
# N, M = map(int, input().split())
# nums = list(map(int,input().split()))
# prefix_sum = []

# for i in range(N):
#     psum = sum(nums[0:i+1])
#     prefix_sum.append(psum)


# for i in range(M):
#     start, end = map(int,input().split())
#     if start != 1:
#         print(prefix_sum[end-1]-prefix_sum[start-2])
#     else: 
#         print(prefix_sum[end-1])