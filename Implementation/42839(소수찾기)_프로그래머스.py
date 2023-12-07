# https://school.programmers.co.kr/learn/courses/30/lessons/42839
# 42839. 소수찾기 [🥈 LEVEL 2]
# 📚 알고리즘 분류: 구현(Implementation)
# ⏰ 걸린 시간 : 20분
# 
# [문제풀이]
# 0. number를 각각 쪼개서 numlist에 저장한다.
# 1. 구할 수 있는 순열을 구해서 permutation 배열에 넣는다. 이때 중복하지 않는지 확인한다.(itertools.permutations)
# 2. 중복하지 않는 값들중에서 check를 통해서 소수를 찾는다.
# 3. 소수를 찾을때 에라토스 테네스의 체로 소수를 찾아 시간복잡도를 낮춘다.
# --------------------------------------------------------------------------------------------------
import itertools
import math
def check(number):
    for i in range(2, int(number**(1/2))+1):
        if number % i ==0:
            return False
    return True
def solution(numbers):
    answer = 0
    numlist = []
    permutation = set()
    for num in numbers:
        numlist.append(num)
    for i in range(1,len(numlist)+1):
        per = list(itertools.permutations(numlist,i))
        # 순열을 찾아 순열의 리스트 만큼 순회한다.
        for j in range(len(per)):
            if int(''.join(per[j])) not in permutation and int(''.join(per[j])) > 1:
                # set에 존재 하지 않는 값 그리고 1 보다 클때만 소수를 검사할 수 있게 해준다.
                permutation.add(int(''.join(per[j])))
                if check(int(''.join(per[j]))):
                    print(int(''.join(per[j])))
                    answer +=1
    return answer

# --------------------------------------------------------------------------------------------------