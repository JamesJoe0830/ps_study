# https://www.acmicpc.net/problem/1475
# 1475. 방 번호 [🥈 실버 5]
# 📚 알고리즘 분류: 배열
# ⏰ 걸린 시간 : 20분 
# 시간복잡도 : O(N)
# 
# [문제풀이]
# 0. 1부터 9까지 인덱스에 num[i] 하나씩 추가해주면 된다.
# 1. 6과 9가 서로 다르면 둘중 하나가 작은 값의 인덱스 카운트를 올린다.
# 
# 
# ----------------------------------------
import sys
input = sys.stdin.readline

nums=list(input().rstrip())

for i in range(len(nums)):
    nums[i] = int(nums[i])
numset = [0]*10

for i in nums:
    if i == int(6) or i == int(9):
        if numset[6] <= numset[9]:
            numset[6] += 1
        else:
            numset[9] += 1
    else:
        numset[i] +=1

print(max(numset))

# ----------------------------------------