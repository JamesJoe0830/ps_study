function solution(my_string, num1, num2) {
    var answer = '';
    Array_my_string1 = [];
    Array_my_string = my_string.split('');
    i = Array_my_string[num1];
    Array_my_string[num1]=Array_my_string[num2];
    Array_my_string[num2]=i;
    answer = Array_my_string.join('');
    return answer;
}