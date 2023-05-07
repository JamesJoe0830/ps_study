# https://www.acmicpc.net/problem/9095 -> 1, 2, 3 더하기 (실버 3) -> DP문제
# <DP인 근거?>
# DP[1], DP[2], DP[3] 이거 이상부터는 점화식 형태로 주어짐 -> DP인 결정적인 증거
#
#
#
# ------------------------------------------------------------------------------
import sys
input = sys.stdin.readline

T = int(input())
DP = [0]*12
DP[1] = 1
DP[2] = 2
DP[3] = 4

answer = []
i = 4
# 점화식으로 DP 정의
while True:
    if DP[11] != 0:
        break
    if i > 3:
        DP[i] = DP[i-1] + DP[i-2] + DP[i-3]
    i += 1


for t in range(T):
    answer.append(DP[int(input())])

# 출력
for _ in range(T):
    print(answer[_])
# ------------------------------------------------------------------------------
