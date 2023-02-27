function solution(sides) {
    var answer = 0;
    var sum = 0;
    
    for(let i =0;i<sides.length;i++){
        sum += sides[i] ;
    }
   // for(let j=0;j<sides.length;j++){
        if(sum>2*Math.max(...sides)){
           answer = 1;
           }
        else if(sum<=2*Math.max(...sides)) {
            answer=2;
        }
    
    
    return answer;
}