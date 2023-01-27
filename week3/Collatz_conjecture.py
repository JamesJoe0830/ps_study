def solution(num):
    answer = 0
    if num ==1:
        answer=0
    else:
        for x in range(500) :
            if num ==1:
                answer=x
                break
            elif num%2 == 0:
                num = num/2
            else :
                num = (num*3) + 1
        if num !=1:
            answer = -1
    return answer