# https://www.acmicpc.net/problem/4673
# 셀프 넘버 (4673번) -> 실버 5 <구현>
# 
# [💡 아이디어 💡]
#  0. 재귀함수 설정: d(75) = 75+7+5 = 87 이때 next 값이 arr에 있고 10000 보다 작으면 recursion
#  1. next 를 없애면 된다. 
# 
# arr 를 set으로 쓰면 시간복잡도 1로 줄어들 것임 
#   
# ---------------------------------------------------------------------------------------------
from collections import deque

arr = deque()
for i in range(1,10000):
    arr.append(i)

# 재귀함수
def recursion(now):
    l=len(str(now))
    next = now
    split = list(map(int,str(now)))
    for i in range(len(split)):
        next += split[i]

    if next in arr  and next < 10000:
        arr.remove(next)
        recursion(next)

# recursion들어가지 않는 것들 확인
for i in range(1,10000):
    if i in arr:
        recursion(i)

# 출력
for i in range(len(arr)):
    print(arr[i])

# ---------------------------------------------------------------------------------------------
