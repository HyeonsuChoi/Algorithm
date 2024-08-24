/*
 * 주어진 정수 배열에서 중복된 요소를 제거하는 함수
 * 
 * 함수명: removeDuplicates
 * 
 * 입력:
 *   int arr[]: 정수 배열 (길이는 1 이상)
 *   int n: 배열의 길이
 *   int* newLength: 중복 제거 후 배열의 길이를 저장할 포인터
 * 
 * 출력:
 *   중복된 요소가 제거된 배열을 반환합니다. 반환된 배열의 길이는 newLength에 저장됩니다.
 *
 * 예시:
 *   int arr[] = {1, 2, 2, 3, 4, 4, 5};
 *   int newLength;
 *   int* result = removeDuplicates(arr, 7, &newLength);
 *   // result는 {1, 2, 3, 4, 5}를 가리키며, newLength는 5가 됩니다.
 *   for(int i = 0; i < newLength; i++) {
 *       printf("%d ", result[i]); // 출력: 1 2 3 4 5
 *   }
 */

#include <stdio.h>
#include <stdlib.h>

int* removeDuplicates(int arr[], int n, int* newLength) {
    if (n == 0) {
        *newLength = 0;
        return NULL;
    }

    // 새로운 배열을 동적으로 할당합니다.
    int* result = (int*)malloc(n * sizeof(int));
    int j = 0;

    // 첫 번째 요소는 무조건 추가
    result[j++] = arr[0];

    // 배열을 순차적으로 비교하면서 중복을 제거
    for (int i = 1; i < n; i++) {
        if (arr[i] != arr[i - 1]) {  // 현재 요소가 이전 요소와 다르면 추가
            result[j++] = arr[i];
        }
    }

    *newLength = j;  // 중복 제거 후 배열의 길이
    return result;
}

int main() {
    int arr[] = {1, 2, 2, 3, 4, 4, 5};  // 입력 배열
    int n = sizeof(arr) / sizeof(arr[0]);  // 배열의 길이
    int newLength;  // 중복 제거 후 배열의 길이
    
    // 중복 제거 함수 호출
    int* result = removeDuplicates(arr, n, &newLength);
    
    // 결과 출력
    printf("중복 제거 후 배열: ");
    for(int i = 0; i < newLength; i++) {
        printf("%d ", result[i]);
    }
    printf("\n");
    
    // 동적 할당된 메모리 해제
    free(result);
    
    return 0;
}