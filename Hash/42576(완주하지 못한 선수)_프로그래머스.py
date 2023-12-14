# https://school.programmers.co.kr/learn/courses/30/lessons/42576
# 42576. 완주하지 못한 선수 [🥈 LEVEL 2]
# 📚 알고리즘 분류: 해쉬
# ⏰ 걸린 시간 : 5분
# 시간 복잡도 : O(n)
# 
# [문제 풀이]
# 0. participant에 선수 중 한명이 완주하지 못했다.
# 1. 참가자, 완주자를 정렬하고 completion에 마지막에 빈값을 추가하면
# 2. 두개의 배열의 길이는 같게되고
# 3. 다른 값이 발견되면 바로 answer로 출력하고 멈춘다.
# -------------------------------------------------------------------------------------

def solution(participant, completion):
    answer = ''
    index = []
    participant.sort()
    completion.sort()
    completion.append("") # completion의 길이는 하나가 짧아서 for 문 하나만 돌리기 위해서 빈 값 추가
    for i in range(len(participant)):
        if participant[i] != completion[i]:
            answer = participant[i]
            break
    return answer

# -------------------------------------------------------------------------------------