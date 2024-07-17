"""
    문자열 뒤집기 (Reverse String)

    문제 설명:
    주어진 문자열을 뒤집는 함수를 작성하세요.

    함수 서명:
    def reverse_string(s: str) -> str:

    입력:
    - `s`: 문자열 (0 <= len(s) <= 1000)

    출력:
    - 주어진 문자열을 뒤집은 문자열을 반환합니다.

    예시:
    >>> reverse_string("hello")
    "olleh"
    >>> reverse_string("Python")
    "nohtyP"
    >>> reverse_string("")
    ""
    >>> reverse_string("a")
    "a"
    
    설명:
    - 첫 번째 예시: "hello"를 뒤집으면 "olleh"가 됩니다.
    - 두 번째 예시: "Python"을 뒤집으면 "nohtyP"가 됩니다.
    - 세 번째 예시: 빈 문자열은 뒤집어도 빈 문자열입니다.
    - 네 번째 예시: 길이가 1인 문자열은 뒤집어도 같은 문자열입니다.
"""

def reverse_string(s: str) -> str:
    return "".join(reversed(s))

print(reverse_string("hello")) 
print(reverse_string("Python"))  
print(reverse_string(""))    
print(reverse_string("a"))  

"""
def reverse_string(s: str) -> str:
    return s[::-1]

print(reverse_string("hello")) 
print(reverse_string("Python"))  
print(reverse_string(""))    
print(reverse_string("a")) 
"""