# https://www.acmicpc.net/problem/1654
# 1654. 랜선 자르기 [실버 2] 
#  
# <이진 탐색(Binary Search)으로 푼이유?>
# 1. 랜선은 합칠 수 없다.
# 2. 랜선을 나눌 수 있는 값을 가장 빠르게 탐색 할 수 있다. (시간복잡도 log(n))
# 3. start와 end 같이지면 멈추고 출력
# -----------------------------------------------------------------------------

import sys 
input = sys.stdin.readline
#K : 랜선의 개수, N: 필요한 랜선의 개수
K, N = map (int, input().split())
LanArr = [int(input()) for i in range(K)]
# 이진 탐색은 정렬이 되어있어야 한다.
LanArr.sort() 

start ,end =1, LanArr[K-1]
while start <= end:
    mid =  (start + end) //2
    lan_cnt = 0 # 랜선의 자르는 개수 총합

    for i in range(K):
        lan_cnt += LanArr[i]//mid
    if lan_cnt >= N:
        start = mid + 1
    elif lan_cnt < N:
        end = mid -1
    print(start,end)

# while문이 끝나고 나면 end 출력
print(end)





# 시간초과 코드 ------------------------------------------------------------------
# K, N = map (int, input().split())
# LanArr = [int(input()) for i in range(K)]
# LanArr.sort()
# # print(LanArr)
# total = sum(LanArr)
# cnt = []
# for i in range(K):
#         cnt.append(total//LanArr[i])
# if N != sum(cnt):
#     count = cnt[K-1]+1
#     divide = LanArr[K-1]//(count)
#     while True:
#         if N == sum(cnt):
#             print(divide)
#             break
#         cnt = []
#         for i in range(K):
#             cnt.append(LanArr[i]//divide)
#         count +=1
# -----------------------------------------------------------------------------