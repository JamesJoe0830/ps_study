# https://school.programmers.co.kr/learn/courses/30/lessons/42746
# 42746. 가장 큰 수 [🥈 LEVEL 2]
# 📚 알고리즘 분류: 정렬(Sort)
# ⏰ 걸린 시간 : 31분
# 
# [문제 풀이]
# 0. numbers의 배열을 내림차순 정렬해준다.
# 1. 이때 정렬 방법으로 lambda를 통해서 string 값인 x를 4번 반복하도록 해주고 비교군은[:4] 까지 비교해 내림차순 정렬한다.
# 2. 비교군은[:4] 까지 비교하도록하는 이유는 제한사항에 numbers의 원소는 0 이상 1,000 이하이기 때문이다.
# 
# --------------------------------------------------------------------------------
# [주의사항]
# permutations는 시간복잡도가 O(n!) 인 경우는 적합하지 않다!
# possible = list(map(''.join,itertools.permutations(numbers,len(numbers))))
import itertools
def solution(numbers):
    answer = ''
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: (x * 4)[:4], reverse=True) 
    # 이 방법은 x를 4번 반복해서 비교 정렬해준다.
    # [:4]이렇게 한 이유는 numbers의 원소는 0 이상 1000이하의 제약 조건을 갖고 있기 때문이다.


    answer = ''.join(numbers)
    if answer[0] == '0':
        answer = '0'

    return str(answer)
# --------------------------------------------------------------------------------