# https://www.acmicpc.net/problem/4949
# 4949. 균형잡힌 세상 [실버4] -> 🧾 STACK
#
# <문제 접근>
# 괄호 열고 닫고니까 stack에 ( or [ 이거 넣어주고  ] ) 이거일때 stack의 -1값 확인해서 짝맞으면 pop 
# 마지막 나왔을때 짝 안맞으면 stack 은 비어있지 않을테니까 no 출력
#
# -----------------------------------------------------------------------------

while True :
    string = input()
    stack = []
    if string == '.':
        break
    for s in string:
        if s == '[' or s == '(':
            stack.append(s)
        elif s == ']':
            if len(stack) != 0 and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(s)
                break   
        elif s == ')':
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(s)
                break
    if stack :
        print('no')
    else:
        print('yes')

        
