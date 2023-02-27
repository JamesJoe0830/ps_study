def solution(a, b, n):
    answer = 0
    re=0
    for i in range(n):
        if n>=a:
            if n%a != 0:
                re= (n//a)*b
                n= (n//a)*b +n-(n//a)*a
                answer += re
            elif n%a ==0:
                re= (n//a)*b
                n= (n//a)*b
                answer += re         
    return answer