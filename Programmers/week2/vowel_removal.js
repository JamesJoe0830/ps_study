function solution(my_string) {
    var answer = [];
    var arr = my_string.split('');
    var vowel = ['a','e','i','o','u'];
    
    for(var i=0;i<arr.length;i++){
        for(var j=0;j<vowel.length;j++){
            if(arr[i] === vowel[j]){
                arr.splice(i,1);
                i--;
            }
        }    
    }
    answer = arr.join('');
    return answer;
}