def solution(numbers):
    answer = 0
    s=0
    for i in range(len(numbers)):
        s += numbers[i]
        answer = 45 - s
    return answer