# https://www.acmicpc.net/problem/11053

# 11053. 가장 긴 증가하는 부분 수열 [🥈 실버2]
# 📚 알고리즘 분류: DP 🔥오답 필요
# ⏰ 걸린 시간 : 43분
# 시간 복잡도 : O(n) 
# [문제 풀이]
# 
# ---------------------------------------------
import sys
input = sys.stdin.readline
N = int(input())
arr = list(map(int,input().split()))

dp = [1]*N #dp가 가장 짧은 순열일때 자기자신인 1 임


for i in range(N):
    cnt = 0
    for j in range(0,i):
        if arr[j]<arr[i]:
            dp[i] = max(dp[i],dp[i]+1)
print(max(dp))
# ---------------------------------------------