# https://acmicpc.net/problem/1337
# 15565. 귀여운 라이언 [🥈 실버 1]
# 📚 알고리즘 분류: 투 포인터
# ⏰ 걸린 시간 : 18분
# 시간복잡도 : O(N)
# 
# [투 포인터 알고리즘 푼 근거 및 회고]
# 0. K개가 있다고 할때 최소의 집합을 결정할때 투포인터를 사용하지 않으면 시간초과 발생
# 
# 
# 문제 풀이
# 0. 정렬시킨다.
# 1. 투 포인터로 start값을 i로 잡고 end값은 N-1로 잡는다.
# 2. 최고로 많이 필요한 점은 4개이다. (answer = 4)
# 3-1. 시작점과 끝점의 차가 5이상이면 end 값을 -1 해준다.
# 3-2. 시작점과 끝점의 차가 4이하이면 정답을 4 - (end-start) [4개가 필요했는데 있는 점은 없애기 위한 것]이 값과 비교해 더 작은 것으로 업데이트
# ------------------------------------------------------------------
import sys

input = sys.stdin.readline

N = int(input())
nums = [int(input()) for _ in range(N)]
nums.sort()
answer = 4 

for i in range(N):
    start = i
    end = N-1
    while start < end:
        if nums[end]-nums[start] > 4:
            end -=1
        else:
            temp_answer = 4 - (end-start)
            answer = min(answer,temp_answer)
            break
print(answer)
# ------------------------------------------------------------------

