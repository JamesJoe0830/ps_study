# https://www.acmicpc.net/problem/1654
# 1654. 랜선 자르기 [🥈 실버 2]
# 📚 알고리즘 분류: 이진 탐색(Binary Search)
# ⏰ 걸린 시간 : 16분
# 
# 
# 0. 결국 1부터 최대까지 탐색하는데 N의 값이 1이상 1,000,000이하이기 때문에
# 1. 탐색의 logN의 시간복잡도를 갖는 이진 탐색(Binary Search)으로 한다.
# 2. 랜선을 각각 mid값으로 나눠서 총 나온 개수를 구한다.
# 3. 랜선의 최대 길이를 구하기 위해서 바로 [if slice_cnt == N]일때 중지하면 안된다.
# 4. 결국 start와 end가 만나는 지점에서 while문이 끝나고 end를 출력하면 된다.
# ----------------------------------------------------------------------

import sys
input = sys.stdin.readline
# K: 이미 갖고 있는 랜선의 개수 N : 필요한 랜선의 개수
K, N = map(int,input().split())
Cables = [int(input()) for _ in range(K)]
Cables.sort()
start = 1
end = Cables[-1]

# 이진 탐색(Binary Search)
while start <= end:
    mid = (start + end)//2 
    slice_cnt = 0
    for c in Cables:
        slice_cnt += c//mid
    if slice_cnt >= N :
        start = mid + 1
    elif slice_cnt < N :
        end = mid - 1
print(end)
# ----------------------------------------------------------------------