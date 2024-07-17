"""
    중복 제거된 리스트 (Remove Duplicates)

    문제 설명:
    주어진 정수 리스트에서 중복된 요소를 제거하고, 각 요소가 한 번씩만 나타나도록 합니다. 
    반환된 리스트는 오름차순으로 정렬되어 있어야 합니다.

    함수 서명:
    def remove_duplicates(nums: list[int]) -> list[int]:

    입력:
    - `nums`: 정수로 구성된 리스트 (0 <= len(nums) <= 1000, -1000 <= nums[i] <= 1000)

    출력:
    - 중복이 제거되고 오름차순으로 정렬된 리스트를 반환합니다.

    예시:
    >>> remove_duplicates([1, 1, 2])
    [1, 2]
    >>> remove_duplicates([4, 3, 2, 1])
    [1, 2, 3, 4]
    >>> remove_duplicates([1, 2, 2, 3, 4, 4, 5])
    [1, 2, 3, 4, 5]
    >>> remove_duplicates([])
    []
    
    설명:
    - 첫 번째 예시: [1, 1, 2]에서 중복된 1을 제거하고, 정렬하여 [1, 2]를 반환합니다.
    - 두 번째 예시: [4, 3, 2, 1]에서 중복된 요소는 없으므로, 정렬하여 [1, 2, 3, 4]를 반환합니다.
    - 세 번째 예시: [1, 2, 2, 3, 4, 4, 5]에서 중복된 2와 4를 제거하고, 정렬하여 [1, 2, 3, 4, 5]를 반환합니다.
    - 네 번째 예시: 빈 리스트는 빈 리스트를 반환합니다.
"""

def remove_duplicates(nums: list[int]) -> list[int]:
        return sorted(set(nums))

print(remove_duplicates([1, 1, 2]))
print(remove_duplicates([4, 3, 2, 1]))
print(remove_duplicates([1, 2, 2, 3, 4, 4, 5]))
print(remove_duplicates([]))