/*
 * 주어진 문자열이 팰린드롬인지 확인하는 함수
 * 
 * 함수명: isPalindrome
 * 
 * 입력:
 *   char str[]: 문자열 (대소문자 구분 없이 팰린드롬 검사)
 * 
 * 출력:
 *   팰린드롬이면 1을 반환하고, 그렇지 않으면 0을 반환합니다.
 *
 * 예시:
 *   char str[] = "madam";
 *   int result = isPalindrome(str);
 *   printf("%d\n", result); // 출력: 1
 *
 *   char str[] = "hello";
 *   result = isPalindrome(str);
 *   printf("%d\n", result); // 출력: 0
 */

#include <stdio.h>
#include <string.h>
#include <ctype.h>

int isPalindrome(char str[]) {
    int len = strlen(str);
    char lowerStr[len + 1];
    char reversedStr[len + 1];

    // 소문자로 변환
    for (int i = 0; i < len; i++) {
        lowerStr[i] = tolower(str[i]);
    }
    lowerStr[len] = '\0'; // 문자열 종료를 명시

    // 문자열 뒤집기
    for (int i = 0; i < len; i++) {
        reversedStr[i] = lowerStr[len - 1 - i];
    }
    reversedStr[len] = '\0'; // 문자열 종료를 명시

    // 문자열 비교
    if (strcmp(lowerStr, reversedStr) == 0)
        return 1;
    else
        return 0;
}

int main() {
    char str[] = "Madam";
    
    // 팰린드롬 검사 함수 호출
    int result = isPalindrome(str);
    
    // 결과 출력
    printf("%s는 팰린드롬인가요? %d\n", str, result); // 예상 출력: 1
    
    return 0;
}