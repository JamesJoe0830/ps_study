import sys
# import math
# import itertools
# N = int(sys.stdin.readline())
# num_zero = 0

# answer=1
# num_zero = N//2 # 00의 개수
# for i in range(1,num_zero+1):
#     answer += math.factorial(N-i)/(math.factorial(i)*math.factorial(N-2*i))
# print(int(answer)%15746)
###### 시간 초과
N = int(sys.stdin.readline())
DP = [0] * 1000001
DP[1] = 1
DP[2] = 2

for i in range(3,N+1):
    DP[i] = (DP[i-1] + DP[i-2]) % 15746

print(DP[N])
