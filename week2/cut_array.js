function solution(numbers, num1, num2) {
    var answer = [];
    for (var i = num1 ; i <= num2 ;i++){
        answer[i-num1] = numbers[i]
    }
    return answer;
}