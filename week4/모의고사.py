def solution(answers):
    answer = []
    a =[1,2,3,4,5]*len(answers)
    b =[2, 1, 2, 3, 2, 4, 2, 5]*len(answers)
    c =[3, 3, 1, 1, 2, 2, 4, 4, 5, 5]*len(answers)
    count_a = count_b = count_c = 0
    arr =[]
    for i in range(len(answers)):
        if answers[i] == a[i]:
            count_a += 1
        if answers[i] == b[i]:
            count_b += 1
        if answers[i] == c[i]:
            count_c += 1
# 여기서 아래부분이 핵심 max 와 arr 가 같다면 각각의 1,2,3을 출력해옴
    arr = [count_a,count_b,count_c]
    cnt = max(count_a, count_b, count_c)
    for j in range(len(arr)) :
        if cnt == arr[j] :
            answer.append(j+1)
    return answer