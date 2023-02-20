def solution(n, m):
    answer = []
    arr = []
    for i in range(1,m+1):
        if n%i ==0 and m%i ==0:
            arr.append(i)
    if len(arr) ==1:
        answer.append(1)
        answer.append(n*m)
    else:
        answer.append(max(arr))
        answer.append(n*(m//max(arr)))
    return answer