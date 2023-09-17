# https://acmicpc.net/problem/3273
# 3273. 두 수의 합 [🥈 실버 3]
# 📚 알고리즘 분류: 투 포인터
# ⏰ 걸린 시간 : 40분 -> 시간초과 메모리초과 발생..
# 시간복잡도 : O(N)
# 
# [문제풀이]
# 0. 정렬시키고 
# 1. start가 end보다 작으면 계속 while을 돈다.
# 2. 합이 x값을 만족하면 start를 +1
# 3. 합이 x값을 초과하면 end를 -1해줌
# 4. 그외에는 계속 start를 +1해줌 
# -----------------------------------------
import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int,input().split()))
x = int(input())
nums.sort()
sum = 0


start = 0
end = n-1
while start < end:
    if nums[start] + nums[end] == x:
        sum +=1
        start +=1 
    elif nums[start] + nums[end] > x:
        end -=1
    else:
        start +=1 
print(sum)

# [시간초과] ------------------------------------
# import sys
# input = sys.stdin.readline

# n = int(input())
# nums = list(map(int,input().split()))
# x = int(input())
# nums.sort()
# sum = 0

# for i in range(n):
#     start = i
#     end = n-1
#     while start < end:
#         if nums[start] + nums[end] == x:
#             sum +=1
#             break
#         else:
#             end -=1
# print(sum)


# [메모리초과] ------------------------------------
# import sys
# from itertools import combinations
# input = sys.stdin.readline

# n = int(input())
# nums = list(map(int,input().split()))
# x = int(input())
# nums.sort()
# combi = list(combinations(nums,2))
# sum = 0
# for a, b in combi:
#     if a+b == x:
#         sum +=1

# print(sum)
# ------------------------------------------