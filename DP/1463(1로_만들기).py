import sys
N = int(sys.stdin.readline())
# Queue = []
# max_value = 1000001
DP = [0]*(N+1)
#bottom up 방식
for i in range(2,N+1):
    DP[i]=DP[i-1]+1 # 1빼는 과정을 역으로 먼저 더해줌
    if i % 2 ==0:
        DP[i] = min(DP[i],DP[i//2]+1)
    if i % 3 ==0:
        DP[i] = min(DP[i],DP[i//3]+1)
print(DP[N])