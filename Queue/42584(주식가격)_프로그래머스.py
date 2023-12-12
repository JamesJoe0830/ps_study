# https://school.programmers.co.kr/learn/courses/30/lessons/42584?language=python3
# 42584. 주식가격 [🥈 LEVEL 2]
# 📚 알고리즘 분류: 큐(Queue)
# ⏰ 걸린 시간 : 5분
# 
# [문제 풀이]
# 0. Q로 접근 해서 푼다.
# 1. check할 주식가격을 뽑고
# 2. 나머지 prices의 값들과 비교를 한다.
# 2-1. 나머지 값들보다 check값이 크다면 값이 떨어졌다는 것이고 그 순간 멈춘다.
# 2-2. 그외에 상황에는 모두 1씩 증가하도록 한다.
# ----------------------------------------------------------------------
from collections import deque
def solution(prices):
    answer = []
    Q = deque(prices)
    while Q:
        cnt=0
        check = Q.popleft()
        for value in Q:
            if check > value :
                cnt+=1
                break
            else:
                cnt +=1
        answer.append(cnt)
    return answer
# ----------------------------------------------------------------------