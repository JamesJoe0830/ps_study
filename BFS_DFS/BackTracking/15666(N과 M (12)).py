# https://www.acmicpc.net/problem/15666
# 15666. N과 M (12) [🥈 실버 2]
# ⏰ 걸린시간 : 15분
# 
# 
# 중복 조합을 구해주는 방법을 구하면 된다.
# 같은 수를 여러번 골라서 써도 되지만, 해당 수를 중복해서 추출하면 안된다.
# combinations_with_replacement 이렇게 하면 nums에서 중복으로 값을 M개 추출한다.
# ------------------------------------------------
import sys
from itertools import combinations_with_replacement
input = sys.stdin.readline

N, M = map(int,input().split())
nums = list(map(int,input().split()))
nums.sort()
answer = []
answer.extend(combinations_with_replacement(nums, M))

answer = sorted(set(answer))

for combi in answer:
    print(* combi)
# ------------------------------------------------