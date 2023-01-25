function solution(my_string) {
    var answer = [];
    let arr=my_string.split('');
    for(let i=0;i<my_string.length;i++){
        answer[my_string.length-i]=arr[i]
    }
    return answer.join('');
}