function solution(order) {
    var answer = 0;
    let order_str=String(order)
    let arr = order_str.split('');
        
    for(var i = 0; i<order_str.length;i++){
        if((arr[i])%3===0){
            if(arr[i]==='0'){
                answer--;   
            }
            answer += 1;   
       }
    }
    return answer;
}