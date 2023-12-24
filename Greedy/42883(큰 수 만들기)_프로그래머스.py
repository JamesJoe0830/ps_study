# https://school.programmers.co.kr/learn/courses/30/lessons/42883?language=python3
# 42883. 큰 수 만들기 [🥈 LEVEL 2]
# 📚 알고리즘 분류: STACK(스택)
# ⏰ 걸린 시간 : 40분 🔥 오답필요
# 
# [풀이 방법]
# 0. 수를 돌면서 stack의 값이 있고 마지막 값이 현재 for문의 값보다 작고 k가 0보다 크면
# 1. 값을 뺀다. k도 -1 씩해준다.
# 2. 모든값은 stack에 넣어주고
# 3. 예외로 k가 0이 아닐 경우 k 만큼 뒤에서 빼면된다.
# 
# [주의 사항]
# 0. combolations로 접근하면 시간초과가 발생한다. O(N^2)
# ----------------------------------------------------------------------------
# import itertools
# nums = list(number)
    # coll = list(map(lambda x : "".join(x),itertools.combinations(nums,len(number)-k)))
    # answer=str(max(coll))

def solution(number, k):
    answer = ''
    stack = []
    for num in number:
        while stack and stack[-1] < num and k>0:
            k-=1
            stack.pop()
        stack.append(num)
    if k != 0 :
        stack = stack[:-k]
    answer = "".join(stack)
        
    return answer