function solution(rsp) {
    var answer = [];
    let arr = rsp.split('');
    for(let i=0;i<rsp.length;i++){
        if(arr[i]==='2'){
            answer[i]=0;
        }
        else  if(arr[i]==='0'){
            answer[i]=5;
        }
        else  if(arr[i]==='5'){
            answer[i]=2;
        }  
    }
    return answer.join('');
}