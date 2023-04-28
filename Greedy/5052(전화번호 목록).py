# https://www.acmicpc.net/problem/5052 (골드 4) 전화번호 목록 => 오답 필요
#<Greedy>
# starts with 메소드 확인해볼 것 

import sys
input = sys.stdin.readline
answer = []
t = int(input())
for _ in range(t):
    n = int(input())
    nums = [input().rstrip() for _ in range(n)] # 각 전화번호 받아서 list에 저장
    nums.sort()
    check ="YES"
    for i in range(len(nums)-1):
        if nums[i] == nums[i+1][0:len(nums[i])]: ## 이부분 오답할때 다시 볼 부분 slicing 
            check = "NO"

    if check == "NO":
        answer.append("NO")
    else:
        answer.append("YES")

for i in range(len(answer)):
    print(answer[i])