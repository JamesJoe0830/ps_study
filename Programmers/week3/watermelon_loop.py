def solution(n):
    answer = []
    for x in range(0,n):
        if x%2 ==0 :
            answer.append('수')
        elif x%2 != 0 :
            answer.append('박')
    return ''.join(answer)