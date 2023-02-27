function solution(my_string) {
    var answer = [];
    let arr = my_string.split('');
    let arr_parseInt=[];

    for(let i =0;i<my_string.length;i++){
        arr_parseInt[i]=parseInt(arr[i],36);
    }
        arr_parseInt.sort(function(a,b){
                return a-b
        });
        
    for(let j =0;j<my_string.length;j++){
        answer[j] = arr_parseInt[j].toString(36); //36진수
    } 
    return answer.join('');
}