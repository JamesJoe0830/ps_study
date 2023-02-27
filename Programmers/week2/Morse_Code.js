function solution(letter) {
    var answer = [];
    let letter_arr=letter.split(' ');
    
    let morse = { 
    '.-':'a', '-...':'b', '-.-.':'c', '-..':'d', '.':'e', '..-.':'f', 
    '--.':'g', '....':'h', '..':'i', '.---':'j', '-.-':'k', '.-..':'l', 
    '--':'m', '-.':'n','---':'o', '.--.':'p', '--.-':'q', '.-.':'r', 
    '...':'s', '-':'t', '..-':'u', '...-':'v', '.--':'w', '-..-':'x', 
    '-.--':'y', '--..':'z'
    };
    for(let i=0;i<letter_arr.length;i++){
        if(letter_arr[i] in morse){  //in 연산자는 객체안을 스캔해주는 것임
             answer.push(morse[letter_arr[i]]); 
// morse라는 obj에서 letter의 배열과 일치하는 값을   answer의 배열로 입력 받아오는 것
        }
    }
    return answer.join('');
}