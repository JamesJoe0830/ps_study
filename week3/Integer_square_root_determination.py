def solution(n):
    answer = 0
    import math
    if math.sqrt(n)==math.ceil(math.sqrt(n)):
        answer = math.pow((math.sqrt(n)+1),2)
    else:
        answer=-1
    return answer