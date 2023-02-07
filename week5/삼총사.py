# arr중에 3개씩 뽑아내는 것을 만들면 끝 
def solution(number):
    answer = 0
    arr = []
    from itertools import combinations
    arr=(list(combinations(number, 3))) #combination의 사용법
    for i in range(len(arr)):
        if sum(arr[i]) ==0:
            answer +=1
    return answer