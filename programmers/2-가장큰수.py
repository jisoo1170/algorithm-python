import pytest
from collections import deque


@pytest.mark.parametrize("numbers, expected", [
    ([6, 10, 2], "6210"),
    ([3, 30, 34, 5, 9], "9534330"),
    ([100, 20, 10], "2414")
])
def test_simple(numbers, expected):
    assert solution(numbers) == expected


# str 대소 비교가 그냥 문자열 하나씩 넘어가면서 비교 하는 거라서 일반 숫자랑 다르다
# 따라서 숫자의 자릿수를 맞춰주고 str로 만들어 비교해주면 정렬할 수 잇다.
def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    print(str(int(''.join(numbers))))
    print(''.join(numbers))
    return str(int('r'.join(numbers)))


if __name__ == "__main__":
    solution(input)
