# https://www.acmicpc.net/problem/1940
# 1940 (주몽) [🧾 정렬]
#
# <✅ 풀이방법>
# 0. 정렬시키고 이중 for문으로 M - Num[i] == Num[j] 이거 갯수 세면 끝
#
# ----------------------------------------------------------------------
import sys

N = int(input())
M = int(input())
Num = list(map(int, input().split()))
Num.sort()

cnt = 0
for i in range(N):
    for j in range(i+1, N):
        if M - Num[i] == Num[j]:
            cnt += 1
            break
print(cnt)

# ----------------------------------------------------------------------
