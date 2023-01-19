function solution(my_string, n) {
    var answer = '';
    let arr = [];
 
    let array_my_string = my_string.split('');
    //let index = 0;
    for(let i=0; i<my_string.length;i++){
        for(let j=0; j<n;j++){
            //arr[index]=array_my_string[i]; //h,e,l,l,o
            //console.log(arr)
            //index++;
            arr.push(array_my_string[i]);//stack push개념 
       }
    }
    answer = arr.join('');
    
    return answer;
}