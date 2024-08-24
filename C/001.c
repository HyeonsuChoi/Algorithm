/*
 * 주어진 정수 배열의 모든 요소를 더하여 그 합을 반환하는 함수
 * 
 * 함수명: sumArray
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
 *   int result = sumArray(arr, 5);
 *   printf("%d\n", result); // 출력: 15
 */

#include <stdio.h>

int sumArray(int arr[], int n) {
    int sum = 0;
    for(int i = 0; i < n; i++){
        sum += arr[i];
    }
    return sum;
}

int main() {
    int arr[] = {1, 2, 3, 4, 5};
    int n = sizeof(arr) / sizeof(arr[0]);
    int result = sumArray(arr, n);
    printf("배열의 합: %d\n", result); // 예상 출력: 15
    return 0;
}s