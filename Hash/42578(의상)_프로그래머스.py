# https://school.programmers.co.kr/learn/courses/30/lessons/42578
# 42578. 의상 [🥈 LEVEL 2]
# 📚 알고리즘 분류: 해쉬
# ⏰ 걸린 시간 : 15분
# 시간 복잡도 : O(n)
# [문제 풀이]
# 두번째 이름이 갖다면 중복해서 사용할 수 없다.
# dictionary를 사용해서 종류에 따라 추가한다.
# --------------------------------------------------------------------
def solution(clothes):
    answer = -1
    combie = 1 
    clothe_dict= dict()
    
    for name, types in clothes:
        if types in clothe_dict:
            clothe_dict[types] +=1
        else: 
            clothe_dict.update({types: 1})
    
    # case1 ) 종류가 2개 이상일때 
    # 0. (각 종류별 개수 + 1) 를 모두 곱한다.
    # 1. +1 을 하는 이유는 해당 종류를 사용하지 않는 경우도 있기 때문이고 
    # 2. 모두 사용하지 않는 경우는 없으므로 answer를 -1로 두고 시작한다.
    if len(clothe_dict) > 1 : 
        for key in clothe_dict:
            combie *= (clothe_dict[key]+1)
        answer += combie
    else:
        answer = len(clothes)

    return answer
# --------------------------------------------------------------------