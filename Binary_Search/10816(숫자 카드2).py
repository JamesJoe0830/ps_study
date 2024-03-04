# https://www.acmicpc.net/problem/10816
# 10816.숫자 카드 2 [🥈 실버 4] -> 👋 오답 필요
# 📚 알고리즘 분류: 이진 탐색
# ⏰ 걸린 시간 : 25분 -> 시간초과 발생
#
# [시간 초과 해결방법]
# 0. 처음에 일치하는 mid값을 찾으면 왼쪽 오른쪽으로 while문을 돌려서 카운트 해주는 방식이에서 시간초과 발생
# 1. bisect 이진탐색 라이브러리로 해결
# 2. bisect_left 해당 값 맨왼쪽 인덱스 찾아줌
# 3. bisect_right 해당 값 맨오른쪽 인덱스 찾아줌
# ✨ bisect 이진탐색 인덱스 값 찾아주는거 유용하다.
#
# --------------------------------------------------------------------------------
import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.readline
N = int(input())
Nums = list(map(int, input().split()))
M = int(input())
Guess = list(map(int, input().split()))
Nums.sort()
answer = []

for i in range(M):
    start = 0
    end = N-1
    cnt = 0
    while start <= end:
        mid = (start+end)//2
        if Guess[i] == Nums[mid]:
            cnt = bisect_right(Nums, Guess[i]) - bisect_left(Nums, Guess[i])
            break
        elif Guess[i] > Nums[mid]:
            start = mid+1
        elif Guess[i] < Nums[mid]:
            end = mid-1
    answer.append(cnt)
print(*answer)

# 시간초과 발생 코드-------------------------------------------------------------------------
# import sys
# N = int(input())
# Nums = list(map(int, input().split()))
# M = int(input())
# Guess = list(map(int, input().split()))
# Nums.sort()
# answer = []

# for i in range(M):
#     start = 0
#     end = N-1
#     cnt = 0
#     while start <= end:
#         mid = (start+end)//2
#         if Guess[i] == Nums[mid]:
#             cnt += 1
#             down = mid-1
#             up = mid+1
#             while down >= 0:
#                 if Guess[i] == Nums[down]:
#                     cnt += 1
#                     down -= 1
#                 else:
#                     break
#             while up <= N-1:
#                 if Guess[i] == Nums[up]:
#                     cnt += 1
#                     up += 1
#                 else:
#                     break
#             break
#         elif Guess[i] > Nums[mid]:
#             start = mid+1
#         elif Guess[i] < Nums[mid]:
#             end = mid-1
#     answer.append(cnt)
# print(*answer)
# --------------------------------------------------------------------------------
