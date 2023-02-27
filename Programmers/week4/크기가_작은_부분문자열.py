def solution(t, p):
    answer = 0
    arr=[]
    for i in range(0,len(t)-len(p)+1): # 0 ~ 4
        arr.append(t[i:len(p)+i])
        if arr[i]<=p :
            answer +=1
    return answer