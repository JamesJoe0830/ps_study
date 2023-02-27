#set 중복 제거해서 돌려줌
def solution(numbers):
    answer = []
    arr =[]
    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
            answer.append(numbers[i]+numbers[j])
    
    answer=sorted(set(answer))
    return answer