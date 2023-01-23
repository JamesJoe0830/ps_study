function solution(n, t) {
    var answer = 0;
    for(let i=0;i<=t;i++){
        answer = n*(2**i);
    }
    return answer;
}