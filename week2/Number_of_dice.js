function solution(box, n) {
    var answer = 0;
    let arr = [];
    for(let i =0;i<box.length;i++){
        arr[i] = parseInt(box[i]/n);
        //answer *= arr[i];
    }
        answer= arr[0]*arr[1]*arr[2]
  
    return answer;
}