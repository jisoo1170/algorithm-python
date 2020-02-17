import pytest


@pytest.mark.parametrize("heights, expected", [
    ([6, 9, 5, 7, 4], [0, 0, 2, 2, 4]),
    ([3, 9, 9, 3, 5, 7, 2], [0, 0, 0, 3, 3, 3, 6]),
    ([1, 5, 3, 6, 7, 6, 5], [0, 0, 2, 0, 0, 5, 6])
])
def test_simple(heights, expected):
    assert solution(heights) == expected


# 바로 이전 송신탑을 돌면서 자신 보다 높은 높이를 만나면 멈춤
def solution(heights):
    answer = []
    for idx, height in enumerate(heights):
        i = idx-1
        while i >= 0:
            if heights[i] > height:
                break
            i -= 1
        answer.append(i+1)

    return answer


if __name__ == "__main__":
    solution(input)
