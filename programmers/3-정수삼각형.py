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


"""
처음에는 재귀로 풀면서 어떤 idx에서 온 값인지 알아야 한다고 생각했는데 그럴 필요가 없었다.

계속 값을 더해주면서 최댓값을 저장해가면 된다.
어떤 값들을 거쳐서 왔는지는 중요하지 않기 때문이다. 그냥 최댓값을 구하는 거라서!

안쪽의 값들은 경로가 여러가지 이기 때문에 최댓값을 저쟁해주면 되고, 그 외 끝에 값들은 그냥 값을 더해주면 된다.
"""
