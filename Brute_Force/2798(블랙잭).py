# https://www.acmicpc.net/problem/2798
# 2798. 블랙잭 [🥉 브론즈 2]
# ⏰ 걸린시간 : 15분
# 
# 
# [풀이방법]
# 0. 3장씩 뽑아서 골라서 합을 구해주고
# 1. 절대값이 가장 작은 값이 가장 가까운 것이다.
# 2. 단, 합이 M보다 크면 안됨
# ------------------------------------------------
import sys
from itertools import combinations
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))

combis=list(set(combinations(nums,3)))
sum_combis = set()
for i in range(len(combis)):
    if sum(combis[i]) <= M:
        sum_combis.add((abs(M-sum(combis[i])),sum(combis[i])))

answer=list(sum_combis)
answer.sort()


print(answer[0][1])
# ------------------------------------------------