/*
 * 주어진 정수 N에 대해 N번째 피보나치 수를 반환하는 함수
 * 
 * 함수명: fibonacci
 * 
 * 입력:
 *   int n: 정수 (0 이상의 수)
 * 
 * 출력:
 *   N번째 피보나치 수를 반환합니다.
 *
 * 예시:
 *   int result = fibonacci(5);
 *   printf("%d\n", result); // 출력: 5 (피보나치 수열: 0, 1, 1, 2, 3, 5, ...)
 */

#include <stdio.h>

int fibonacci(int n) {
    if (n == 0) return 0;
    if (n == 1) return 1;
    
    int a = 0;
    int b = 1;
    int result;
    
    for (int i = 2; i <= n; i++) {
        result = a + b;
        a = b;
        b = result;
    }
    
    return result;
}

int main() {
    int num = 5;
    
    // 피보나치 함수 호출
    int result = fibonacci(num);
    
    // 결과 출력
    printf("%d번째 피보나치 수: %d\n", num, result); // 예상 출력: 5
    
    return 0;
}