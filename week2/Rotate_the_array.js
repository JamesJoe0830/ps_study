function solution(numbers, direction) {
    var answer = [];
    for(let i=0;i<numbers.length;i++){ 
        for(let j=i+1;j<numbers.length;j++){
            if(direction==="right"){
                answer[j]=numbers[i];
                answer[0]=numbers[numbers.length-1];
                answer;
                console.log(answer);
            } 
            else if(direction==="left"){
                answer[i]=numbers[j];
               // numbers[numbers.length-1]=numbers[0];
            }
        }
    }
    for(let i=0;i<numbers.length;i++){ 
        for(let j=i-1;j<numbers.length;j++){
             if(direction==="left"){
                answer[j]=numbers[i];
                answer[numbers.length-1]=numbers[0];
                answer;
             }
        }
    }
    return answer;
}