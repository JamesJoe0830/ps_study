def solution(X, Y):
    answer = ''
    # sort()함수를 안 쓰기 위해 i를 9부터 아래 0까지 for문
    for i in range(9,-1,-1) :
        # 문자열 * 숫자 => 반복되는 문자열 더하기 
        # min() => 둘의 겹치는 숫자 중 더 작은 횟수가 합쳐져야 하므로!! 
        answer += (str(i) * min(X.count(str(i)), Y.count(str(i))))

    if answer == '' :
        return '-1'
    # 문자열에 0만 존재할 경우 처리
    elif len(answer) == answer.count('0'):
        return '0'
    else :
        return answer