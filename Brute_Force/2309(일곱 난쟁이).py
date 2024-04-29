# https://www.acmicpc.net/problem/2309 -> 일곱 난쟁이(실버1) 브루트 포스
# <문제 풀이>

# -----------------------------------------------------------------------------
import sys
input = sys.stdin.readline

members = [] # 난쟁이 멤버 리스트
pop_mem = [] # 빼야될 인덱스
sum = -100
for i in range(9):
    member = int(input())
    members.append(member)
    sum += member
members.sort()


for i in range(len(members)):
    if len(pop_mem) == 2: # 해당 테스트 케이스가 여러개일 경우 더 들어가는 것을 막음
        break
    for j in range(i+1,len(members)):
        if members[i] + members[j] == sum:
            pop_mem.append(i)
            pop_mem.append(j)
            break

# 출력 
for m in range(9):
    if m not in pop_mem:
        print(members[m])
# -----------------------------------------------------------------------------

# 3
# 16
# 12
# 19
# 20
# 22
# 8
# 9
# 33