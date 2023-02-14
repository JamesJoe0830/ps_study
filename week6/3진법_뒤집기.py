def solution(n):
    answer = 0
    arr = []
    if n<3:
        answer = n
    while n>=3 :
        arr.append(n%3) 
        if n//3 < 3 :
            arr.append(n//3)
        n=n//3
    for i in range(len(arr)):
        answer += (3**(len(arr)-(i+1)))*arr[i]
    return answer