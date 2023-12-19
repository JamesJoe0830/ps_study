# https://school.programmers.co.kr/learn/courses/30/lessons/1845
# 1845. 포켓몬 [🥈 LEVEL 1]
# 📚 알고리즘 분류: 해쉬
# ⏰ 걸린 시간 : 3분
# 시간 복잡도 : O(nlogn) 
# [문제 풀이]
# 0. 정렬한다.
# 1. 앞뒤의 값을 비교해가면서 만약 같은 값이 나왔다면 0으로 만들고
# 2. 0이 아닌 nums의 값을 구한다.
# 3. 그 후 절반보다 작을때 count를 answer로 그렇지 않을때는 절반 값을 answer로 한다.
# -------------------------------------------------------------------

def solution(nums):
    answer = ''
    arr = []
    count = 0
    nums.sort()
    for i in range(len(nums)-1):
        if (nums[i] == nums[i+1]):
            nums[i] = 0 
    for k in nums:
        if k !=0 :
            count += 1
    if count <= len(nums)/2:
        answer = count
    else:
        answer = len(nums)/2
    return answer
# -------------------------------------------------------------------