# https://www.acmicpc.net/problem/1475
# 1475. 방 번호 [🥈 실버 5]
# 📚 알고리즘 분류: 구현(Implementation)
# ⏰ 걸린 시간 : 5분
# 
# [문제풀이]
# 0. Nums 배열 1부터 9 인덱스별로 개수를 셀 수 있는 배열을 만들고
# 1. 지속적으로 9와 6만 대체가 가능하므로 개수중 작은게 있다면 대체해주고
# 2. 그게 아니라면 인덱스에 하나씩 더해서 가장 큰 nums를 출력
# --------------------------------------------------------------------------------------------------

import sys
input = sys.stdin.readline

N = input().rstrip()
nums = [0]*10
for i in N :
  if i == '9' :
    if nums[int(i)] > nums[6] :
      nums[6] +=1
    else :
      nums[int(i)] += 1
  elif i == '6' :
    if nums[int(i)] > nums[9] :
      nums[9] +=1
    else :
      nums[int(i)] += 1
  else:
    nums[int(i)] +=1
print(max(nums))

# --------------------------------------------------------------------------------------------------