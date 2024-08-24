/*
 * 주어진 정수가 소수인지 아닌지를 판별하는 함수
 * 
 * 함수명: isPrime
 * 
 * 입력:
 *   int n: 정수 (1 이상의 수)
 * 
 * 출력:
 *   주어진 정수가 소수이면 1을 반환하고, 그렇지 않으면 0을 반환합니다.
 *
 * 예시:
 *   int result = isPrime(7);
 *   printf("%d\n", result); // 출력: 1 (7은 소수)
 *   
 *   result = isPrime(10);
 *   printf("%d\n", result); // 출력: 0 (10은 소수가 아님)
 */

#include <stdio.h>
#include <math.h>

int isPrime(int n) {
    if (n <= 1) return 0; // 1은 소수가 아닙니다.
    if (n <= 3) return 1; // 2와 3은 소수입니다.
    if (n % 2 == 0 || n % 3 == 0) return 0; // 2 또는 3으로 나누어지면 소수가 아닙니다.
    
    // 5부터 sqrt(n)까지 검사합니다.
    for (int i = 5; i * i <= n; i += 6) {
        if (n % i == 0 || n % (i + 2) == 0) return 0; // 6k ± 1 검사
    }
    return 1; // 위 조건을 통과하면 소수입니다.
}

int main() {
    int num = 7;
    
    // 소수 판별 함수 호출
    int result = isPrime(num);
    
    // 결과 출력
    printf("%d는 소수인가요? %d\n", num, result); // 예상 출력: 1 (7은 소수)
    
    num = 10;
    result = isPrime(num);
    printf("%d는 소수인가요? %d\n", num, result); // 예상 출력: 0 (10은 소수가 아님)
    
    return 0;
}