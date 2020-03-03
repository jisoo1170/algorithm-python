import pytest


def solution(N):
    answer = 0
    num = [1, 1]
    for i in range(N-1):
        num.append(num[i]+num[i+1])
    print(num)
    answer = (num[-1] + num[-2])*2
    return answer


@pytest.mark.parametrize("N, expected", [
    (5, 26),
    (6, 42)
])
def test_simple(N, expected):
    assert solution(N) == expected
