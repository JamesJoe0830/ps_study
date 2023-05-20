# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AWZ2IErKCwUDFAUQ&categoryId=AWZ2IErKCwUDFAUQ&categoryType=CODE&problemTitle=&orderBy=RECOMMEND_COUNT&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=3
# 5948. 새샘이의 7-3-5 게임 [D3] -> 정렬
# 
# 
# 
# -----------------------------------------------------------------------------
import sys
input = sys.stdin.readline

T = int(input())

def Check(nums):
    Plus = []
    for i in range(7):
        for j in range(i+1,7):
            for k in range(j+1,7):
                if nums[i]+nums[j]+nums[k] not in Plus:
                    Plus.append(nums[i]+nums[j]+nums[k])
    Plus.sort(reverse=True)

    return Plus[4]

for tc in range(1,T+1):
    nums = list(map(int,input().split()))
    nums.sort(reverse=True)


    print('#{} {}'.format(tc,Check(nums)))




