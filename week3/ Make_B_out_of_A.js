function solution(before, after) {
    var answer = 0;
    let arr_before=before.split('');
    let arr_after=after.split('');
    arr_before.sort();
    arr_after.sort();
    let count =0;
    
    for(let i=0; i<arr_before.length;i++){
        if(arr_before[i] === arr_after[i]){
            count ++;
        }
    }
    if(count===before.length){
        answer=1;
    }
    
    return answer;
}