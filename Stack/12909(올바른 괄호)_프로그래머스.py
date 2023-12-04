# https://school.programmers.co.kr/learn/courses/30/lessons/12909
# 12909. 올바른 괄호 [🥈 LEVEL 2]
# 📚 알고리즘 분류: STACK(스택)
# ⏰ 걸린 시간 : 14분
# 
# [스택인 이유?]
# 0. '(' 인 경우에 넣고 ')' 인 경우에 뺀다.
# 1. 모든 값을 다 확인했는데 stack에 값이 남아있다면 올바르지 않은 값인 것이다.
# 2. ❗️ 하나 체크해야할 사항) stack이 비어있는데 뺄 경우
#   2-1. 이런 경우는 '(' 가 없는데 ')'이렇게 시작하는 경우라서 바로 중단하고 False를 반환한다.
# ----------------------------------------------------------------------------

def solution(s):
    answer = True
    stack = []
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(s[i])
        else:
            if stack :
                stack.pop()
            else :
                answer = False
                break
    if stack :
        answer = False
    return answer

# ----------------------------------------------------------------------------