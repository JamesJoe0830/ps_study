def solution(s):
    answer = ''
    numbers = {'zero':0,'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9}
    arr=[]
    for i in range(len(s)):
        if s[i].isalpha(): #이게 숫자인지 확인
            arr.append(s[i])
            print(arr)
            if ''.join(arr) in numbers.keys():
                answer += str(numbers[''.join(arr)])
                arr =[]
                print('if',answer)
        else:
            answer += s[i]
    return int(answer)