function solution(hp) {
    var answer = 0;
   
    const General = 5;
    const Soldier = 3;
    const Ergate = 1;
    
    answer = Math.floor(hp/General) + Math.floor((hp%General)/Soldier) +
            Math.floor((hp%General)%Soldier)/Ergate;
     return answer;
}