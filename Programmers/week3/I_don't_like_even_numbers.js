function solution(n) {
    var answer = [];
    if(n%2 != 0){
        for(let i=0;i<=Math.floor(n/2);i++){
          answer[i]=2*i+1;
        }
    }
    else if(n%2 === 0){
         for(let i=0;i<Math.floor(n/2);i++){
          answer[i]=2*i+1;
        }
    }
    return answer;
}