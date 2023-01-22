function solution(my_string) {
    var answer = [];
    let arr = my_string.split('');
    
    for(let i=0; i< my_string.length;i++){
        if(arr[i]===arr[i].toUpperCase()){
            answer[i]=arr[i].toLowerCase();
        }
        else if(arr[i] != arr[i].toUpperCase()){
            answer[i]=arr[i].toUpperCase();
        }
    }
    return answer.join('');
}