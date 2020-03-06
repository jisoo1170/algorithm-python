import pytest


def solution(triangle):
    for i in range(1, len(triangle)):
        for j in range(i+1):
            print(i, j)
            # 왼쪽 끝의 경우
            if j == 0:
                triangle[i][j] += triangle[i-1][j]
            # 오른쪽 끝의 경우
            elif j == i:
                triangle[i][j] += triangle[i-1][j-1]
            else:
                triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])
    return max(triangle[-1])


@pytest.mark.parametrize("triangle, expected", [
    ([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]], 30)
])
def test_simple(triangle, expected):
    assert solution(triangle) == expected
