def solution(s):
    answer = 0
    count = 0
    print(ord('9'))
    for i in range(len(s)):
        if(ord(s[i])>=48 and ord(s[i])<=57):
            count += 1
            print(count)
    if count == len(s) and (len(s) == 4 or len(s) ==6):
        answer =True
    else:
        answer = False
    return answer