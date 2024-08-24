/*
 * 주어진 정수 배열에서 특정 값을 찾아 해당 값의 인덱스를 반환하는 함수
 * 
 * 함수명: findIndex
 * 
 * 입력:
 *   int arr[]: 정수 배열 (길이는 1 이상)
 *   int n: 배열의 길이
 *   int target: 찾고자 하는 값
 * 
 * 출력:
 *   값이 존재하면 해당 값의 인덱스를 반환하고, 그렇지 않으면 -1을 반환합니다.
 *
 * 예시:
 *   int arr[] = {1, 2, 3, 4, 5};
 *   int result = findIndex(arr, 5, 3);
 *   printf("%d\n", result); // 출력: 2 (3은 배열의 2번째 인덱스에 있습니다.)
 *
 *   result = findIndex(arr, 5, 6);
 *   printf("%d\n", result); // 출력: -1 (6은 배열에 없습니다.)
 */

#include <stdio.h>

int findIndex(int arr[], int n, int target) {
    for(int i = 0; i < n; i++){
        if(arr[i] == target)
            return i;
    }
    return -1;
}

int main() {
    int arr[] = {1, 2, 3, 4, 5};
    int n = sizeof(arr) / sizeof(arr[0]);
    
    // 값을 찾는 함수 호출
    int target = 3;
    int result = findIndex(arr, n, target);
    
    // 결과 출력
    printf("%d의 인덱스: %d\n", target, result); // 예상 출력: 2
    
    target = 6;
    result = findIndex(arr, n, target);
    printf("%d의 인덱스: %d\n", target, result); // 예상 출력: -1
    
    return 0;
}