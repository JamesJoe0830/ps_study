def solution(s):
    answer = []
    list_s=list(s)
    arr=[]
    for i in range(0,len(s)): #5 4 3 2 1
        arr.append(s.rfind(s[i],0,i))
        if arr[i] != -1:
            answer.append(i-arr[i])
        else: 
            answer.append(arr[i])
    return answer