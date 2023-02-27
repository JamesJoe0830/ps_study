# 날짜 카운트는 i번째때 score 길이로 알아서 측정
def solution(k, score):
    answer = []
    arr=[]
    for i in range(len(score)):
        if not arr:
            arr.append(score[0])
        else:
            arr.append(score[i])
            arr.sort(reverse=True)
        if len(arr) < k:
            answer.append(min(arr))
        elif len(arr) >= k:
            answer.append(arr[k-1])
    return answer