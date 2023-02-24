import sys
N = int(sys.stdin.readline())
ex_rank, rank =[], []
answer=0
for i in range(N):
    a = int(sys.stdin.readline())
    ex_rank.append(a)
    rank.append(i+1)
ex_rank.sort()
for i in range(N):
    answer = answer + abs(rank[i]-ex_rank[i])
print(answer)