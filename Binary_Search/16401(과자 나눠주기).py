# https://www.acmicpc.net/problem/16401
# 16401. 과자 나눠주기 [🥈 실버 2]
# 📚 알고리즘 분류: 이진 탐색(Binary Search)
# ⏰ 걸린 시간 : 22분
# 
# [풀이방법]
# 0. 전형적인 이분 탐색이다.
# 1. start와 end 값으로 해당 조건을 만족하는지 계속해서 탐색하면 된다.
# 2. for문은 다음과 같다.
# 3. 쿠키가 만약 자르고자 하는 크키보다 작다면, cnt를 자르는데 cookie를 자르는 크기인 mid 만큼 자른다.
# ----------------------------------------------------------------------------------

import sys 
input = sys.stdin.readline

M, N = map(int,input().split())
cookies = list(map(int,input().split()))

start = 1
end = max(cookies) #최대로 자르는 쿠키 크기

while start <= end :
    mid = (start + end)//2 #쿠키 자르는 크기
    cnt = 0
    for cookie in cookies :
        if mid <= cookie :
            cnt += cookie//mid
    if cnt >= M :
        start = mid + 1
    else:
        end = mid - 1
print(end)

# ----------------------------------------------------------------------------------