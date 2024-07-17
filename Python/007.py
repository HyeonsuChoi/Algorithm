"""
    정렬된 배열 병합 (Merge Sorted Arrays)

    문제 설명:
    두 개의 정렬된 정수 배열이 주어졌을 때, 이 배열들을 하나의 정렬된 배열로 병합하는 함수를 작성하세요.

    함수 서명:
    def merge_sorted_arrays(arr1: list[int], arr2: list[int]) -> list[int]:

    입력:
    - `arr1`: 정렬된 정수 배열 (0 <= len(arr1) <= 1000)
    - `arr2`: 정렬된 정수 배열 (0 <= len(arr2) <= 1000)

    출력:
    - 두 배열이 병합된 정렬된 배열을 반환합니다.

    예시:
    >>> merge_sorted_arrays([1, 3, 5], [2, 4, 6])
    [1, 2, 3, 4, 5, 6]
    >>> merge_sorted_arrays([0, 1], [3, 4])
    [0, 1, 3, 4]
    >>> merge_sorted_arrays([], [1, 2, 3])
    [1, 2, 3]
    >>> merge_sorted_arrays([1, 2, 3], [])
    [1, 2, 3]
    >>> merge_sorted_arrays([], [])
    []

    설명:
    - 첫 번째 예시: [1, 3, 5]와 [2, 4, 6]을 병합하여 [1, 2, 3, 4, 5, 6]을 반환합니다.
    - 두 번째 예시: [0, 1]과 [3, 4]를 병합하여 [0, 1, 3, 4]를 반환합니다.
    - 세 번째 예시: 빈 배열과 [1, 2, 3]을 병합하여 [1, 2, 3]을 반환합니다.
    - 네 번째 예시: [1, 2, 3]과 빈 배열을 병합하여 [1, 2, 3]을 반환합니다.
    - 다섯 번째 예시: 두 빈 배열을 병합하여 빈 배열을 반환합니다.
"""

def merge_sorted_arrays(arr1: list[int], arr2: list[int]) -> list[int]:
    mergedArr = arr1 + arr2
    return sorted(mergedArr)

print(merge_sorted_arrays([1, 3, 5], [2, 4, 6]))
print(merge_sorted_arrays([0, 1], [3, 4]))
print(merge_sorted_arrays([], [1, 2, 3]))
print(merge_sorted_arrays([1, 2, 3], []))
print(merge_sorted_arrays([], []))