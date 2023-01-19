function solution(my_string, letter) {
    var answer = '';
     Array_my_string = my_string.split('')
    for(var i =0;i< my_string.length;i++)
       if(Array_my_string[i]===letter){
            Array_my_string[i] ='';
       }
           answer= Array_my_string.join('');      
            
        
    return answer;
}
