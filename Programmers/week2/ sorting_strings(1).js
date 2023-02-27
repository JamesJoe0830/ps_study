function solution(my_string) {
    var answer = [];
    let arr1 = [];
    let arr = my_string.split('');
    let h = 0;
    for (let i =0; i<my_string.length; i++){
        if(arr[i]<10 && arr[i]>=0){
            arr1.push(Number(arr[i])); 
           // console.log(answer);
        }
    }
          if (arr1.length===1){
              answer= arr1;
            }
    for(let j =0; j<arr1.length-1; j++){ //0 1 2 3 4 
        for(let k =j+1; k<arr1.length; k++){ // 1 2 3 4 5
            let h = 0;
            if(arr1[j]>arr1[k]){
                h = arr1[j];
                arr1[j]=arr1[k];
                arr1[k]= h;
                console.log("arr1 : ",arr1)
            }
        }
            answer=arr1;
    }
    return answer;
}