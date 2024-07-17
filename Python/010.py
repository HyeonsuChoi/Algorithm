"""
    누락된 숫자 찾기 (Find the Missing Number)

    문제 설명:
    0부터 n까지의 숫자가 포함된 길이 n의 배열이 주어졌을 때, 배열에서 누락된 숫자를 찾는 함수를 작성하세요. 
    배열에는 숫자가 중복되지 않고, 오직 하나의 숫자가 누락되어 있습니다.

    함수 서명:
    def find_missing_number(nums: list[int]) -> int:

    입력:
    - `nums`: 정수로 구성된 배열 (0 <= len(nums) <= 10^4, 0 <= nums[i] <= n)

    출력:
    - 배열에서 누락된 숫자를 반환합니다.

    예시:
    >>> find_missing_number([3, 0, 1])
    2
    >>> find_missing_number([0, 1])
    2
    >>> find_missing_number([9,6,4,2,3,5,7,0,1])
    8
    >>> find_missing_number([0])
    1

    설명:
    - 첫 번째 예시: [3, 0, 1]에서 2가 누락되었습니다.
    - 두 번째 예시: [0, 1]에서 2가 누락되었습니다.
    - 세 번째 예시: [9,6,4,2,3,5,7,0,1]에서 8이 누락되었습니다.
    - 네 번째 예시: [0]에서 1이 누락되었습니다.
"""

def find_missing_number(nums: list[int]) -> int:
    numList = sorted(nums)
    firstNum = 0
    for num in numList:
        if firstNum == num:
            firstNum += 1
        elif firstNum != num:
            return firstNum
    return firstNum

print(find_missing_number([3, 0, 1]))
print(find_missing_number([0, 1]))
print(find_missing_number([9,6,4,2,3,5,7,0,1]))
print(find_missing_number([0]))

"""
def find_missing_number(nums: list[int]) -> int:
    n = len(nums)
    total_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return total_sum - actual_sum

print(find_missing_number([3, 0, 1])) 
print(find_missing_number([0, 1]))     
print(find_missing_number([9, 6, 4, 2, 3, 5, 7, 0, 1]))  
print(find_missing_number([0]))       
"""