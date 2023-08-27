# https://www.acmicpc.net/problem/15649
# 15649. N과 M (1) [🥈 실버 3]
# ⏰ 걸린시간 : 8분
# 
# 순열로 구하면 된다.
# ------------------------------------------------
import sys
from itertools import permutations
input = sys.stdin.readline

N, M = map(int, input().split())
nums = []
visited =[]
for i in range(1, N+1):
    nums.append(i)
visited.extend(list(permutations(nums,M)))

for permu in visited:
    print(* permu)
# ------------------------------------------------