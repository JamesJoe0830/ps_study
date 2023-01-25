function solution(array) {
    var answer = 0;
    array.sort(function(a,b){
        return a-b
    });
    answer=array[(array.length/2)-0.5];
    return answer;
}