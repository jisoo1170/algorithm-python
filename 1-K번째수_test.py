import pytest


@pytest.mark.parametrize("array, commands, expected", [
    ([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]], [5, 6, 3])
])
def test_simple(array, commands, expected):
    assert solution(array, commands) == expected


def solution(array, commands):
    answer = []
    for command in commands:
        # 배열에 담겨있는 변수를 한 번에 받을 수도 있음
        i, j, k = command
        before_list = array[i-1:j]
        before_list.sort()
        answer.append(before_list[k-1])

    return answer


if __name__ == "__main__":
    solution(input)
