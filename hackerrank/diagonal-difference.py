import pytest


def diagonalDifference(arr):
    idx1 = 0
    idx2 = -1
    sum1 = 0
    sum2 = 0
    for a in arr:
        sum1 += a[idx1]
        sum2 += a[idx2]
        idx1 += 1
        idx2 -= 1
    return abs(sum1-sum2)


@pytest.mark.parametrize("arr, expected", [
    ([[11, 2, 4], [4, 5, 6], [10, 8, -12]], 15)
])
def test_simple(arr, expected):
    assert diagonalDifference(arr) == expected
