import sys
input = sys.stdin.readline
N, M = map(int, input().split())
books = list(map(int, input().split()))
path = 0
books.sort()
plus = list()
minus = list()
# print(books)
for i in range(N):
    if books[i] > 0:
        plus.append(books[i])
    else:
        minus.append(books[i])
plus.sort(reverse=True)
# print('+',plus)
# print('-',minus)

if abs(books[0]) > abs(books[-1]): # 음수의 값이 더 큰 경우
    for i in range(0,len(plus),M):
        # print('+일부',plus[i])
        path += 2*plus[i]
    for i in range(0,len(minus),M):
        # print('-일부',minus[i])
        path += 2*abs(minus[i])
    path = path - abs(books[0])
else:                              # 양수의 값이 더 크거나 같은 경우
    for i in range(0,len(plus),M):
        # print('+일부',plus[i])
        path += 2*plus[i]
    for i in range(0,len(minus),M):
        # print('-일부',minus[i])
        path += 2*abs(minus[i])
    path = path - abs(books[-1])
print(path)