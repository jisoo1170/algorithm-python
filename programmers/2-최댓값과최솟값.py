import pytest


def solution(s):
    input = s.split()
    input = list(map(int, input))
    # print(min(input))
    answer = ''
    answer = str(min(input)) + ' ' + str(max(input))
    return answer


@pytest.mark.parametrize("s, expected", [
    ("1 2 3 4", "1 4"),
    ("-1 -2 -3 -4",	"-4 -1"),
    ("-1 -1", "-1 -1")
])
def test_simple(s, expected):
    assert solution(s) == expected
