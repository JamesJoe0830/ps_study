function solution(n) {
    var answer = 0;
    var n_string = String(n); //"1234"
   // var b = new Array();
   // var b = [];     //[ ]
   // var c = 0;
    for(var i = 0;i < n_string.length;i++){
      //  b[i] = Number(a[i]); //[1,2,3,4]
      //  c = Number(b[i]);
        answer += Number(n_string[i]); 
    }
    return answer;
}å