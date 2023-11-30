# https://school.programmers.co.kr/learn/courses/30/lessons/42586?language=python3
# 42586. 기능개발 [🥈 LEVEL 2]
# 📚 알고리즘 분류: 큐(Queue)
# ⏰ 걸린 시간 : 30분
# 
# [문제 풀이]
# 0. Q로 접근 해서 푼다.
# 1. 비교값을 정하고 뒤에 남은 값들이 비교값보다 크가나 같을 경우 cnt를 올려준다.
# 2. cnt 올린만큼 Q에서 pop해주기 
# 3. 값이 작다면 멈추고 다음 while문으로 돈다.
import math
from collections import deque
def solution(progresses, speeds):
    answer = []
    Q = deque()
    for i in range(len(progresses)):
        Q.append(math.ceil((100 - progresses[i]) / speeds[i]))

    while Q :
        cnt = 1
        compare = Q.popleft() #비교할 값을 정해준다.
        for i in range(len(Q)):
            # print(Q[i])
            if compare >= Q[i]: #만일 비교 값이 Q 남아있는 뒤에 값들을 비교해서 크거나 같으면 cnt + 1
                cnt +=1 
            else:               #값이 작다면 멈춘다.
                break
        if cnt != 1:            
            for i in range(cnt-1): #cnt 더해준 만큼 Q에서 popleft
                Q.popleft()
                
        answer.append(cnt)    

    return answer