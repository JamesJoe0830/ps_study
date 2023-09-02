# https://www.acmicpc.net/problem/1253
# 1253. 좋다 [🥇 골드 4] -> 🔥 오답 필요(해설 보고 품)
# 📚 알고리즘 분류: 투 포인터
# ⏰ 걸린 시간 : 시간초과 (자기 자신을 제외한 배열을 만들어주는 부분 어려움)
# 시간복잡도 : 투 포인터 -> O(ElogV) : EV인데 우선순위 큐 사용해주면 탐색이 logV로 줄어든다.
#         
# 
# [투 포인터 알고리즘 푼 근거 및 회고]
# 0. 투 포인터로 접근 하려고 했는데 반례가 발생하였다. 
# <반례>
# 4
# 0 0 0 0
# output: 4
# 
# 문제풀이
# 0. A 리스트를 정렬한다.
# 1. 0부터 N-1 까지 반복문을 통해 특정 원소(A[i])를 선택하고, 해당 원소를 제외한 리스트를 생성한다.
# 2. except_self 리스트에서 투 포인터를 이용하여 두 원소의 합이 nums[i]와 같다면 answer를 증가시킨다.
# 3. total이 A[i]보다 작다면 start 1증가
# 4. total이 A[i]보다 크다면 end 1 감소
# ------------------------------------------------------------------
import sys
input = sys.stdin.readline
N = int(input())
nums = list(map(int,input().split()))
nums.sort()
answer = 0
for i in range(N):
    except_self = nums[:i]+nums[i+1:] #자기 자신을 제외한 배열 생성
    start = 0
    end = len(except_self) -1

    while start < end:
        total = except_self[start] + except_self[end]
        if total == nums[i]:
            answer +=1 
            break
        
        elif total < nums[i]: # nums배열보다 total이 작을 경우에 start값을 늘려준다.  # 1 2 3 4 6에서 현재 nums[i]가 6면 start 1 end 4 일떄 
            start +=1
        else: # 지속적으로 하나씩 뺴줌 
            end -=1
print(answer)
# ------------------------------------------------------------------


# 40분 동안 오류 발생한 코드 ---------------------------------------------
# 반례 존재함
# arr = set()
# for i in range(N):
#     for j in range(i+1,N):
#         if nums[i]+nums[j] <= nums[N-1]:
#             if nums[i]+nums[j] in nums:
#                 arr.add(nums[i]+nums[j])
# print(len(arr))
# -------------------------------------------------------------------




