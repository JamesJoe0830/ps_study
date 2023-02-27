#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
int c = 0;
int solution(int n, int k) {
    int answer = 0;
   int c = n / 10 ;
if (n < 10)
   answer = n * 12000 + k * 2000;
else if(n >= 10)
    answer = n * 12000 + (k-c) * 2000;
    
    
    return answer;
}