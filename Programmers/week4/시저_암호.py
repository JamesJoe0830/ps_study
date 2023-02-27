def solution(s, n):
    answer = []
    list_s=list(s)
    for i in range(len(list_s)):
        if((ord(list_s[i]) <= 90 and ord(list_s[i])>= 65)):
            if(ord(list_s[i])+n> 90):
                answer.append(chr(ord(list_s[i])+n-26))
            else:
                answer.append(chr(ord(list_s[i])+n))
        elif((ord(list_s[i]) <= 122 and ord(list_s[i]) >=97)):
            if(ord(list_s[i])+n> 122):
                answer.append(chr(ord(list_s[i])+n-26))
            else:
                answer.append(chr(ord(list_s[i])+n))
        elif(list_s[i] == ' '):
            answer.append(' ')
    return ''.join(answer)