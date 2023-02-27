function solution(age) {
    var answer = [];
     let age_str=String(age);
    let arr=age_str.split('');
    //console.log(arr);
    let obj = {'0':'a', '1':'b', '2':'c', '3':'d', '4':'e', '5':'f', '6':'g', '7':'h', '8':'i', '9':'j'}; // 객체로 각각을 선언
    for(let k =0; k<age_str.length;k++){
        if(arr[k] in obj){ //in 연산자는 객체 안을 스캔
            answer.push(obj[arr[k]]);
        }
      }
    return answer.join('');
}