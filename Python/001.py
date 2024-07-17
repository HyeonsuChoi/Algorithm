
"""
    배열의 합 계산

    문제 설명:
    정수 배열 `arr`이 주어졌을 때, 배열의 모든 원소의 합을 계산하는 함수를 작성하세요.

    함수 서명:
    def sum_array(arr: list[int]) -> int:

    입력:
    - `arr`: 정수로 구성된 배열 (0 <= len(arr) <= 100, -1000 <= arr[i] <= 1000)

    출력:
    - 배열 `arr`의 모든 원소의 합을 반환합니다.

    예시:
    >>>sum_array([1, 2, 3, 4, 5])
    15
    >>>sum_array([-1, -2, -3, -4, -5])
    -15
    >>>sum_array([0, 0, 0, 0])
    0
    >>>sum_array([])
    0
"""

def sum_array(arr: list[int]) -> int:
    sum = 0
    for num in arr:
        sum = sum + num
    return sum 

print(sum_array([1, 2, 3, 4, 5]))
print(sum_array([-1, -2, -3, -4, -5]))
print(sum_array([0, 0, 0, 0]))
print(sum_array([]))

"""
def sum_array(arr: list[int]) -> int:
    return sum(arr)

print(sum_array([1, 2, 3, 4, 5]))
print(sum_array([-1, -2, -3, -4, -5]))
print(sum_array([0, 0, 0, 0]))
print(sum_array([]))
"""