def solution(arr, divisor):
    answer = []
    arr.sort()
    for x in range(len(arr)):
        if arr[x]%divisor ==0:
            answer.append(arr[x])
    if answer ==[]:
         answer=[-1] 
    return answer