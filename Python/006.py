"""
    회문 문자열 검사 (Palindrome Check)

    문제 설명:
    주어진 문자열이 회문인지 확인하는 함수를 작성하세요. 회문이란 앞에서 읽으나 뒤에서 읽으나 동일한 문자열을 의미합니다.
    대소문자를 구분하지 않으며, 영문자와 숫자만을 검사 대상으로 합니다. 공백이나 구두점은 무시합니다.

    함수 서명:
    def is_palindrome(s: str) -> bool:

    입력:
    - `s`: 문자열 (0 <= len(s) <= 1000)

    출력:
    - 주어진 문자열이 회문이면 True, 아니면 False를 반환합니다.

    예시:
    >>> is_palindrome("A man, a plan, a canal: Panama")
    True
    >>> is_palindrome("race a car")
    False
    
    설명:
    - 첫 번째 예시: "A man, a plan, a canal: Panama"은 알파벳 문자만 고려하면 "amanaplanacanalpanama"로 회문입니다.
    - 두 번째 예시: "race a car"는 알파벳 문자만 고려하면 "raceacar"로 회문이 아닙니다.
"""
import re

def is_palindrome(s: str) -> bool:
    newStr = re.sub(r"[^a-zA-Z]", "", s.lower().replace(" ", ""))
    
    if(newStr == newStr[::-1]):
        return True
    else:
        return False
    
print(is_palindrome("A man, a plan, a canal: Panama"))
print(is_palindrome("race a car"))

"""
import re

def is_palindrome(s: str) -> bool:
    # 알파벳 소문자와 숫자만 남기고 모두 제거
    newStr = re.sub(r"[^a-z0-9]", "", s.lower())
    # 뒤집은 문자열과 비교하여 회문 여부 반환
    return newStr == newStr[::-1]

print(is_palindrome("A man, a plan, a canal: Panama"))
print(is_palindrome("race a car"))                    

"""