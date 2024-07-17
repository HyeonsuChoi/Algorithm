"""
    가장 긴 공통 접두사 (Longest Common Prefix)

    문제 설명:
    주어진 문자열 배열에서 가장 긴 공통 접두사를 찾는 함수를 작성하세요. 
    만약 공통 접두사가 없다면 빈 문자열을 반환합니다.

    함수 서명:
    def longest_common_prefix(strs: list[str]) -> str:

    입력:
    - `strs`: 문자열 배열 (0 <= len(strs) <= 200, 0 <= len(strs[i]) <= 200)

    출력:
    - 주어진 문자열 배열에서 가장 긴 공통 접두사를 반환합니다. 공통 접두사가 없다면 빈 문자열을 반환합니다.

    예시:
    >>> longest_common_prefix(["flower", "flow", "flight"])
    "fl"
    >>> longest_common_prefix(["dog", "racecar", "car"])
    ""
    >>> longest_common_prefix(["interspecies", "interstellar", "interstate"])
    "inters"
    >>> longest_common_prefix(["throne", "dungeon"])
    ""
    >>> longest_common_prefix(["throne", "throne"])
    "throne"
    
    설명:
    - 첫 번째 예시: "flower", "flow", "flight"의 가장 긴 공통 접두사는 "fl"입니다.
    - 두 번째 예시: "dog", "racecar", "car"는 공통 접두사가 없습니다.
    - 세 번째 예시: "interspecies", "interstellar", "interstate"의 가장 긴 공통 접두사는 "inters"입니다.
    - 네 번째 예시: "throne", "dungeon"은 공통 접두사가 없습니다.
    - 다섯 번째 예시: "throne", "throne"의 가장 긴 공통 접두사는 "throne"입니다.
"""

def longest_common_prefix(strs: list[str]) -> str:
    if strs == "":
        return ""
    
    first = strs[0]
    last = strs[-1]

    i = 0
    while i < len(first) and i < len(last) and len(first) == len(last):
        i += 1

    return first[:i]

print(longest_common_prefix(["flower", "flow", "flight"]))
print(longest_common_prefix(["dog", "racecar", "car"]))
print(longest_common_prefix(["interspecies", "interstellar", "interstate"]))
print(longest_common_prefix(["throne", "dungeon"]))
print(longest_common_prefix(["throne", "throne"]))

"""
def longest_common_prefix(strs: list[str]) -> str:
    if not strs:
        return ""

    prefix = strs[0]

    for string in strs[1:]:
        while string.find(prefix) != 0:
            prefix = prefix[:-1]
            if not prefix:
                return ""

    return prefix

print(longest_common_prefix(["flower", "flow", "flight"]))  
print(longest_common_prefix(["dog", "racecar", "car"]))
print(longest_common_prefix(["interspecies", "interstellar", "interstate"]))  
print(longest_common_prefix(["throne", "dungeon"]))
print(longest_common_prefix(["throne", "throne"])) 
"""