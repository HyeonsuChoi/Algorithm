"""
    피보나치 수열 (Fibonacci Sequence)

    문제 설명:
    피보나치 수열은 첫 번째와 두 번째 항이 1이며, 그 이후의 항은 바로 앞 두 항의 합으로 정의되는 수열입니다.
    주어진 정수 n에 대해 피보나치 수열의 n번째 항을 반환하는 함수를 작성하세요.
    
    함수 서명:
    def fibonacci(n: int) -> int:

    입력:
    - `n`: 정수 (1 <= n <= 30)

    출력:
    - 피보나치 수열의 n번째 항을 반환합니다.

    예시:
    >>> fibonacci(1)
    1
    >>> fibonacci(2)
    1
    >>> fibonacci(3)
    2
    >>> fibonacci(10)
    55
    
    설명:
    - 첫 번째 예시: n = 1일 때, 첫 번째 피보나치 수는 1입니다.
    - 두 번째 예시: n = 2일 때, 두 번째 피보나치 수는 1입니다.
    - 세 번째 예시: n = 3일 때, 세 번째 피보나치 수는 2입니다.
    - 네 번째 예시: n = 10일 때, 열 번째 피보나치 수는 55입니다.
"""

def fibonacci(n: int) -> int:
    fibonacciNums = [1, 1]
    if n == 1 or n == 2:
        return 1
    for index in range(1, n):
        fibonacciNums.append(fibonacciNums[index] + fibonacciNums[index - 1])
    return fibonacciNums[n - 1]

print(fibonacci(1))
print(fibonacci(2))
print(fibonacci(3))
print(fibonacci(10))

"""
def fibonacci(n: int) -> int:
    if n == 1 or n == 2:
        return 1

    a, b = 1, 1
    for _ in range(n - 2):
        a, b = b, a + b

    return b

print(fibonacci(1))  # 예상 출력: 1
print(fibonacci(2))  # 예상 출력: 1
print(fibonacci(3))  # 예상 출력: 2
print(fibonacci(10))  # 예상 출력: 55
"""