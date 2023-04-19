# https://www.acmicpc.net/problem/1541 -> 잃어버린 괄호(Greedy) 실버 2 -> 오답 필요
# <접근 방법>
# -를 기준으로 다음 -가 발견되기 직전까지 괄화쳐주면 된다.
# <풀이 방법>
# 

# ------------------------------------------------------------
import sys
input = sys.stdin.readline
problem = input().split('-')
answer= 0

# problem[0].split("+") -> 오답시 체크할 부분
for i in problem[0].split("+"):
    answer += int(i)


#-> 오답시 체크할 부분
for i in problem[1:]:
    for j in i.split('+'):
        answer -= int(j)
print(answer)

# ------------------------------------------------------------



# for i in range(len(problem)):
#     if problem[i] != '-' and problem[i] != '+' and problem[i] != "\n":
#         answer += problem[i]
#     else:
#         arr.append(int(answer))
#         arr.append(problem[i])
#         answer= ''
# print(arr)

# for i in range(len(arr)):
#     if arr[i] 