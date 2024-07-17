"""
    두 수의 합 (Two Sum)

    문제 설명:
    정수 배열 `nums`와 정수 `target`이 주어졌을 때, 두 수를 더하여 `target`이 되는 두 수의 인덱스를 찾는 함수를 작성하세요.
    각 입력에 정확히 하나의 답이 있다고 가정하며, 동일한 요소를 두 번 사용할 수 없습니다.

    함수 서명:
    def two_sum(nums: list[int], target: int) -> list[int]:

    입력:
    - `nums`: 정수로 구성된 배열 (2 <= len(nums) <= 10^4, -10^9 <= nums[i] <= 10^9)
    - `target`: 정수 (-10^9 <= target <= 10^9)

    출력:
    - 두 수의 인덱스로 구성된 리스트를 반환합니다. 인덱스는 0부터 시작합니다.

    예시:
    >>> two_sum([2, 7, 11, 15], 9)
    [0, 1]  # nums[0] + nums[1] == 9
    >>> two_sum([3, 2, 4], 6)
    [1, 2]  # nums[1] + nums[2] == 6
    >>> two_sum([3, 3], 6)
    [0, 1]  # nums[0] + nums[1] == 6
    
    설명:
    - 첫 번째 예시: [2, 7, 11, 15]에서 두 수 2와 7을 더하면 9가 되므로 인덱스 0과 1을 반환합니다.
    - 두 번째 예시: [3, 2, 4]에서 두 수 2와 4를 더하면 6이 되므로 인덱스 1과 2를 반환합니다.
    - 세 번째 예시: [3, 3]에서 두 수 3과 3을 더하면 6이 되므로 인덱스 0과 1을 반환합니다.
"""

def two_sum(nums: list[int], target: int) -> list[int]:
    origin = 0
    index = 0
    indexList = []
    for i in range(index, len(nums)):
        origin = nums[i]
        for j in range(index + 1, len(nums)):
            if(origin + nums[j] == target):
                indexList.append(i)
                indexList.append(j)
                return indexList

    return "입력된 숫자가 조건에 맞지 않습니다."

print(two_sum([2, 7, 11, 15], 9))
print(two_sum([3, 2, 4], 6))
print(two_sum([3, 3], 6))

"""
def two_sum(nums: list[int], target: int) -> list[int]:
    # 값 -> 인덱스 매핑을 위한 딕셔너리
    num_to_index = {}
    
    for index, num in enumerate(nums):
        # 필요한 값 (target - 현재 숫자)
        required_num = target - num
        
        # 필요한 값이 딕셔너리에 있다면, 결과를 반환
        if required_num in num_to_index:
            return [num_to_index[required_num], index]
        
        # 현재 숫자를 딕셔너리에 추가
        num_to_index[num] = index
    
    return "입력된 숫자가 조건에 맞지 않습니다."

print(two_sum([2, 7, 11, 15], 9))  # [0, 1]
print(two_sum([3, 2, 4], 6))       # [1, 2]
print(two_sum([3, 3], 6))          # [0, 1]

"""