# https://school.programmers.co.kr/learn/courses/30/lessons/42747
# 42747. H-Index [🥈 LEVEL 2]
# 📚 알고리즘 분류: 정렬(Sort)
# ⏰ 걸린 시간 : 31분
# 
# [문제 풀이]
# 0. answer 의 값을 citations(논문 배열)의 최대값으로 설정해준다. 
# 0-1. [🔑 POINT] answer의 값을 최대값을 원하고있고 빼면서 체크해주기 위해서 최대값으로 설정해주는 것이다. 
# 1. h번 이상 인용된 논문이 h편 이상이고 나머지 논문이 h번 이하 인용되었다면 h 값이므로 바로 멈추고
# 2. 그렇지 않을때 -1 씩 해준다.
# 
# --------------------------------------------------------------------------------

def solution(citations):
    answer = max(citations)
    citations.sort()
    now = 0

    while True:
        for i in range(len(citations)-1):
            if citations[i] <= answer < citations[i+1]:
                if citations[i] == answer:
                    now = i
                else : 
                    now = i + 1
                break
        if len(citations) - now >= answer and now <= answer:
            break
        else:
            answer -=1
            
    return answer
# --------------------------------------------------------------------------------