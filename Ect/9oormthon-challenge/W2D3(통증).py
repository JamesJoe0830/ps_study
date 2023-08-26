# https://level.goorm.io/exam/195690/%ED%86%B5%EC%A6%9D/quiz/1
import sys
input = sys.stdin.readline

N = int(input())
item = 0

if N // 14 >= 1:
    item += N // 14
    N = N % 14
if N // 7 >= 1:
    item += N // 7
    N = N % 7
item += N

print(item)
