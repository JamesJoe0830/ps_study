def solution(nums):
    answer = []
    arr = []
    count = 0
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if(nums[i] == nums[j]):
                nums[i] = 0
    for k in nums:
        if k !=0 :
            count += 1
    if count <= len(nums)/2:
        answer = count
    else:
        answer = len(nums)/2
    return answer