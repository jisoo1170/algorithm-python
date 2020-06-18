import pytest
from collections import Counter


def solution(arr):
    temp = dict(Counter(arr))
    temp = sorted(temp.items())
    # temp 형태가 [(), ()] 이런식으로 바뀜
    answer = max(temp, key=lambda x: x[1])
    return answer[0]


@pytest.mark.parametrize("arr, expected", [()])
def test_simple(arr, expected):
    assert solution(arr) == expected
