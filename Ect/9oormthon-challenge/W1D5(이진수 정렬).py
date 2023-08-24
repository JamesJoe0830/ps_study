import sys
input = sys.stdin.readline
N, K = map(int,input().split())
arr = list(map(int,input().split()))
binary = []

# arr.sort(reverse=True)
for i in arr:
    binary.append((list(bin(i)).count('1'),i))

binary.sort(reverse=True)

print(binary[K-1][1])