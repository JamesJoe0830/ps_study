# https://www.acmicpc.net/problem/2504
# 괄호의 값 (2504번) -> 실버1 <구현> 🔥오답필요
# 
# [문제]
# 0. ‘()’ 인 괄호열의 값은 2이다.
# 1. ‘[]’ 인 괄호열의 값은 3이다.
# 2. ‘(X)’ 의 괄호값은 2×값(X) 으로 계산된다.
# 3. ‘[X]’ 의 괄호값은 3×값(X) 으로 계산된다.
# 4. 올바른 괄호열 X와 Y가 결합된 XY의 괄호값은 값(XY)= 값(X)+값(Y) 로 계산된다.
# 
# [아이디어]
#  0. temp에 ( 만나면 2 곱해주고 / [ 만나면 3 곱해주고 
#  1. )를 (뒤에 바로 만나면 answer에 temp를 더해주고 temp를 2로 나눠줌
# ----------------------------------------------------------------------------------------
import sys
input = sys.stdin.readline 
Bracket = list(input())
stack = []
answer = 0
temp = 1

    # temp에 ( 만나면 2 곱해주고 / [ 만나면 3 곱해주고 
    # )를 (뒤에 바로 만나면 answer에 temp를 더해주고 temp를 2로 나눠줌
for i in range(len(Bracket)):
    if Bracket[i] == '(':
        temp *=2
        stack.append(Bracket[i])
    elif Bracket[i] == '[':
        temp *=3
        stack.append(Bracket[i])
    elif Bracket[i] == ')':
        if not stack or stack[-1] == "[":
            answer = 0
            break
        if Bracket[i-1] =='(':
            answer += temp
        stack.pop()
        temp = temp //2 
    elif Bracket[i] == ']':
        if not stack or stack[-1] == "(":
            answer = 0
            break
        if Bracket[i-1] == '[':
            answer += temp
        stack.pop()
        temp = temp // 3

# 만일 stack에 값이 있다면 answer=0
if stack:
    answer = 0
    print(answer)
else:
    print(answer)
        

