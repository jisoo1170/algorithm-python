import pytest


def solution(ar):
    max_num = max(ar)
    return ar.count(max_num)


@pytest.mark.parametrize("ar, expected", [
    ([3, 2, 1, 3], 2)
])
def test_simple(ar, expected):
    assert solution(ar) == expected
