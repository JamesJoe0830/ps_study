function solution(cipher, code) {
    var answer = [];
    let arr_cipher=cipher.split('');

    for(let i=0;i<cipher.length;i++){
        if((i+1)%code===0)
            answer.push(arr_cipher[i]);
    }
    return answer.join('');
}