function solution(n)
{
    var answer = 0;
    let text=n.toString();
    let arr=text.split('');
    
    for(i=0;i<arr.length;i++){
        answer += Number(arr[i]);
    }
    return answer;
}