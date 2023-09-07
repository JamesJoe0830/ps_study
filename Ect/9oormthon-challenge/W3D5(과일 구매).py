import sys
input = sys.stdin.readline

N, K = map(int, input().split())
fullness = []

for i in range(N):
    P, C = map(int, input().split())
    fullness.append((C // P, P))

fullness.sort(reverse=True)

answer = 0
for full, price in fullness:
    # print(full, price)
    count = min(K, price) # 남은 물건 개수와 물건의 가격중 작은 값 결정
    answer += full * count
    K -= count
    if K == 0:
        break

print(answer)