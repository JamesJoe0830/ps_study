def solution(s):
    answer = ''
    import math
    if(len(s)%2 == 0):
        for i in range(len(s)//2 - 1,len(s)//2 + 1):
            answer += s[i]
    else:
        for i in range(math.ceil(len(s)/2)-1,math.ceil(len(s)/2)):
            answer = s[i]
    return answer