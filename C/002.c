/*
 * 주어진 정수 배열을 제자리에서 뒤집는 함수
 * 
 * 함수명: reverseArray
 * 
 * 입력:
 *   int arr[]: 정수 배열 (길이는 1 이상)
 *   int n: 배열의 길이
 * 
 * 출력:
 *   배열을 제자리에서 뒤집습니다. 별도의 반환값은 없습니다.
 *
 * 예시:
 *   int arr[] = {1, 2, 3, 4, 5};
 *   reverseArray(arr, 5);
 *   // arr은 이제 {5, 4, 3, 2, 1}입니다.
 */

#include <stdio.h>

void reverseArray(int arr[], int n) {
    int left = 0;
    int right = n - 1;

    while(left < right){
        int temp = arr[left];
        arr[left] = arr[right];
        arr[right] = temp;

        left++;
        right--;
    }
}

int main() {
    int arr[] = {1, 2, 3, 4, 5};
    int n = sizeof(arr) / sizeof(arr[0]);
    
    // 배열 뒤집기 함수 호출
    reverseArray(arr, n);
    
    // 결과 출력
    printf("뒤집어진 배열: ");
    for(int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n"); // 예상 출력: 5 4 3 2 1
    
    return 0;
}