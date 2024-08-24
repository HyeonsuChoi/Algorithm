/*
 * 주어진 문자열을 제자리에서 뒤집는 함수
 * 
 * 함수명: reverseString
 * 
 * 입력:
 *   char str[]: 문자열 (길이는 1 이상)
 * 
 * 출력:
 *   문자열을 제자리에서 뒤집습니다. 별도의 반환값은 없습니다.
 *
 * 예시:
 *   char str[] = "hello";
 *   reverseString(str);
 *   // str은 이제 "olleh"입니다.
 */

#include <stdio.h>
#include <string.h>

void reverseString(char str[]) {
    int left = 0;
    int right = strlen(str)- 1;
    char temp;

    while(left < right){
        temp = str[left];
        str[left] = str[right];
        str[right] = temp;

        left++;
        right--;
    }
}

int main() {
    char str[] = "hello";
    
    // 문자열 뒤집기 함수 호출
    reverseString(str);
    
    // 결과 출력
    printf("뒤집어진 문자열: %s\n", str); // 예상 출력: olleh
    
    return 0;
}