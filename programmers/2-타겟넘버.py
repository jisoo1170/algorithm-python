import pytest


def solution(numbers, target):
    global answer
    answer = 0
    global len_num
    len_num = len(numbers)-1
    global t
    t = target
    drf(numbers, 0)
    return answer


def drf(numbers, idx):
    print(numbers)
    if idx > len_num:
        if sum(numbers) == t:
            print("rk")
            global answer
            answer += 1
        return
    else:
        drf(numbers, idx+1)
        numbers[idx] *= -1
        drf(numbers, idx+1)


@pytest.mark.parametrize("numbers, target, expected", [
    ([1, 1, 1, 1, 1], 3, 5),
    ([1, 2, 3], 0, 2)
])
def test_simple(numbers, target, expected):
    assert solution(numbers, target) == expected
