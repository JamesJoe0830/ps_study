# https://school.programmers.co.kr/learn/courses/30/lessons/42587?language=python3
# 42587. 프로세스 [🥈 LEVEL 2]
# 📚 알고리즘 분류: 큐(Queue)
# ⏰ 걸린 시간 : 20분
# 
# [문제 풀이]
# 0. Q로 접근 해서 푼다.
# 1. Q에 값을 넣어줄 때 우선순위와 현재 인덱스값을 넣어준다.
# 2. while문에서 값을 FIFO로 꺼낼때 만일 maxPriority와 일치하는 값이라면
# 3. 빠지는 answer값을 하나 올리고 
# 3-1. 이때 값이 location과 일치한다면 return answer를 해준다.
# 4. 만일 maxPriority와 일치하지 않는다면 다시 빼서 뒤로 넣어준다.
# ----------------------------------------------------------------------
from collections import deque
def solution(priorities, location):
    answer = 0
    Q = deque()
    for i in range(len(priorities)):
        Q.append((priorities[i],i))
    while Q :
        maxPriority = max(Q)[0]
        (priority, index) = Q.popleft()
        if priority == maxPriority :
            answer +=1
            if index == location : 
                return answer
        else :
            Q.append((priority, index))
    print(Q)

    return answer
# ----------------------------------------------------------------------