def divisor(a):
    count=0
    for i in range(1,int(a**(1/2))+1): # 제곱근으로 넣어주면 시간초과 해결 가능
        if a%i ==0:
            if a//i ==i: # 제곱근일 경우 
                count +=1
            else:        # 제곱근이 아닐 경우
                count +=2
    return count
def solution(number, limit, power):
    answer = 0
    numbers = []
    arr = []
    for i in range(1,number+1):
        arr.append(divisor(i))
    for i in range(len(arr)):
        if arr[i] > limit:
            arr[i] = power
        answer +=arr[i]
    return answer