# answer=min(score) * score 개수 * 상자의 개수
# 사과 개수 m으로 나누는 값 나머지 생길 때 안생길때 경우 나누기
def solution(k, m, score):
    answer = 0
    arr =[]
    score.sort(reverse=True)
    for i in range(0,len(score)//m):
        arr.append(min(score[m*i:m*(i+1)])*m)
        # answer=sum(arr) 해당 코드를 하면 시간초과 나옴 아래 for문으로 해결
    for j in arr:
        answer += j
    return answer