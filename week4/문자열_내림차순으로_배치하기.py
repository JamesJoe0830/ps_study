def solution(s):
    answer = ''
    list_s = list(s)
    for i in range(len(s)):
        for j in range(i+1,len(s)):
            if(ord(list_s[i]) < ord(list_s[j])):
                a=list_s[i]
                list_s[i]=list_s[j]
                list_s[j]=a
        answer = list_s
    return ''.join(answer)