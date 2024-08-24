/*
 * 주어진 문자열에서 단어의 개수를 세는 함수
 * 
 * 함수명: countWords
 * 
 * 입력:
 *   char str[]: 문자열 (공백으로 구분된 단어들로 구성됨)
 * 
 * 출력:
 *   문자열 내 단어의 개수를 반환합니다.
 *
 * 예시:
 *   char str[] = "Hello World This is C";
 *   int result = countWords(str);
 *   printf("%d\n", result); // 출력: 5
 */

#include <stdio.h>

int countWords(char str[]) {
    int count = 0;
    int inWord = 0;

    for(int i = 0; i < strlen(str); i++){
        if(str[i] != ' '){
            if(inWord == 0){
                inWord = 1;
                count++;
            }
        } else {
            inWord = 0;
        }
    }
    return count;
}

int main() {
    char str[] = "Hello World This is C";
    
    // 단어 개수 세기 함수 호출
    int result = countWords(str);
    
    // 결과 출력
    printf("단어의 개수: %d\n", result); // 예상 출력: 5
    
    return 0;
}