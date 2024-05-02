# https://www.acmicpc.net/problem/1476 -> 날짜 계산(실버 5) Brute Force
# 
# 
# --------------------------------------------------------------------------
import sys
input = sys.stdin.readline

E,S,M = map(int,input().split())
e = 15
s = 28
m = 19

year = 1

# 계속 연도 더해주면서 나올때까지 더하는 반복문 -> 브루트포스
while True:
    if (year-E) % e ==0 and (year-S) % s ==0 and (year-M) % m == 0 :
        print(year)
        break
    year += 1


# --------------------------------------------------------------------------
