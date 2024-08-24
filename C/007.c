/*
 * 주어진 정수 배열의 모든 요소를 재귀를 사용하여 더하는 함수
 * 
 * 함수명: recursiveSum
 * 
 * 입력:
 *   int arr[]: 정수 배열 (길이는 1 이상)
 *   int n: 배열의 길이
 * 
 * 출력:
 *   배열 요소의 합을 반환합니다.
 *
 * 예시:
 *   int arr[] = {1, 2, 3, 4, 5};
 *   int result = recursiveSum(arr, 5);
 *   printf("%d\n", result); // 출력: 15
 */

#include <stdio.h>

int recursiveSum(int arr[], int n) {
    if(n == 0)
        return 0;
    
    return arr[n - 1] + recursiveSum(arr, n - 1);
}

int main() {
    int arr[] = {1, 2, 3, 4, 5};
    int n = sizeof(arr) / sizeof(arr[0]);
    
    // 재귀를 사용한 배열 합계 함수 호출
    int result = recursiveSum(arr, n);
    
    // 결과 출력
    printf("배열의 합: %d\n", result); // 예상 출력: 15
    
    return 0;
}