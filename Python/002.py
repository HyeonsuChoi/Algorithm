
"""
    중복 없는 가장 긴 부분 문자열

    문제 설명:
    주어진 문자열에서 중복 문자가 없는 가장 긴 부분 문자열의 길이를 구하는 함수를 작성하세요.
    여기서 부분 문자열은 문자열 내에서 연속된 문자들의 집합을 의미합니다. 
    예를 들어, 문자열 "abcabcbb"의 부분 문자열은 "abc", "bca", "cab", 등입니다.
    부분 문자열 내에 같은 문자가 두 번 이상 포함되지 않도록 합니다.

    함수 서명:
    def length_of_longest_substring(s: str) -> int:

    입력:
    - `s`: 문자열 (0 <= len(s) <= 1000)
      - 문자열은 알파벳 소문자와 숫자, 그리고 공백으로 이루어질 수 있습니다.

    출력:
    - 중복 문자가 없는 가장 긴 부분 문자열의 길이를 반환합니다.

    예시:
    >>> length_of_longest_substring("abcabcbb")
    3  # "abc" 또는 "bca" 또는 "cab" 중 하나
    >>> length_of_longest_substring("bbbbb")
    1  # "b"
    >>> length_of_longest_substring("pwwkew")
    3  # "wke" 또는 "kew"
    >>> length_of_longest_substring("")
    0  # 빈 문자열의 길이는 0
    >>> length_of_longest_substring("au")
    2  # "au"
    
    설명 추가:
    - 첫 번째 예시: "abcabcbb"에서는 "abc"가 중복 문자가 없는 가장 긴 부분 문자열입니다. 이 문자열의 길이는 3입니다.
    - 두 번째 예시: "bbbbb"에서는 중복되지 않은 문자는 "b" 하나뿐이므로, 길이는 1입니다.
    - 세 번째 예시: "pwwkew"에서는 중복되지 않은 부분 문자열 "wke"가 가장 길며, 길이는 3입니다.
    - 네 번째 예시: 빈 문자열의 경우, 길이는 0입니다.
    - 다섯 번째 예시: "au"는 중복되지 않은 두 문자가 모두 포함된 부분 문자열로 길이는 2입니다.
"""

def length_of_longest_substring(s: str) -> int:
    n = len(s)
    char_set = set()
    left = 0
    max_length = 0
    
    for right in range(n):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)
    
    return max_length

print(length_of_longest_substring("abcabcbb"))
print(length_of_longest_substring("bbbbb"))
print(length_of_longest_substring("pwwkew"))
print(length_of_longest_substring(""))
print(length_of_longest_substring("au"))