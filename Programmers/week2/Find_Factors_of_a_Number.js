function solution(n) {
    var answer = [];
    for(let i = 0;i<=n;i++){
        if(n%i===0){
            answer.push(i) ;
            console.log(answer)
        }
    }
    return answer;
}