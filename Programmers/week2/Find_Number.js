function solution(num, k) {
    var answer = 0;
    let num_str=String(num);
    let k_str=String(k)
    let arr=num_str.split('');
    //console.log(arr);
    for(var i =0;i<num_str.length;i++){
       if(arr[i]===k_str){
            answer = i+1;
           break; // 찾으면 반복문을 멈춤
         }
        else if(arr[i] != k_str){
            answer=-1;
        }
    }
    return answer;
}