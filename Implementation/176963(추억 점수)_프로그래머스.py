# https://school.programmers.co.kr/learn/courses/30/lessons/176963
# 42586. 기능개발 [🥈 LEVEL 1]
# 📚 알고리즘 분류: 구현(Implementation)
# ⏰ 걸린 시간 : 4분
# 
# [문제 풀이]
# 0. 각각 row에 접근해서 문제를 풀고
# 1. element가 name에 속했다면 인덱스 값을 찾아서 yearning에 값을 뽑아서 더해준다.
# ------------------------------------------------------------------
def solution(name, yearning, photo):
    answer = []
    for row in photo:
        sum = 0
        for element in row:
            if element in name:
                sum += yearning[name.index(element)]
        answer.append(sum)
    return answer
# ------------------------------------------------------------------