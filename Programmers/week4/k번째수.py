def solution(array, commands):
    answer = []
    for j in range(len(commands)):
        arr= commands[j]
        func = []
        for i in range(arr[0]-1,arr[1]):
            func.append(array[i])
            func.sort()
        answer.append(func[arr[2]-1])
    return answer