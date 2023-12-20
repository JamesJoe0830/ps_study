# https://school.programmers.co.kr/learn/courses/30/lessons/42577
# 42577. 전화번호 목록 [🥈 LEVEL 2]
# 📚 알고리즘 분류: 해쉬
# ⏰ 걸린 시간 : 23분
# 시간 복잡도 : O(n) 
# [문제 풀이]
# 0. 정렬한다.
# 1. 앞뒤의 값을 비교해가면서 만약 앞의 값 길이만큼 잘라서 비교했을때
# 2. 같은값이 존재한다면 answer값을 False로 한다.
# [포인트]
# 앞뒤만 비교해도 되는 이유는 접두어가 같다면 앞뒤로 배치된다. 
# -------------------------------------------------------------------

def solution(phone_book):
    answer = True
    n = len(phone_book)
    phone_book.sort()
    for i in range(n-1):
        if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
                answer = False
        
    return answer
# -------------------------------------------------------------------