# https://www.acmicpc.net/problem/10992 (브론즈3) -> 별찍기
# 

import sys
input = sys.stdin.readline

N = int(input())

if N ==1 :
    print("*")
elif N==2:
    print("*","\n")
    print("***")
print("*")
for i in range(N):
    print("*")