function solution(array) {
    var answer = [];
     
    console.log(array)
    
        answer[0]=Math.max(...array);
    for(let i=0; i<array.length;i++){    
        if(array[i]===answer[0]){
            answer[1]=i;
        }
    }
    
    return answer;
}