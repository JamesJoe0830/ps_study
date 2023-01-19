function solution(my_string) {
    var answer = 0;
    Arr= my_string.split('')
    for(let i =0;i<my_string.length;i++){
    if (Number(Arr[i]) <10 && Number(Arr[i])>0){
        answer += Number(Arr[i]);
    
      }
    }
    return answer;
}