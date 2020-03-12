import pytest


def solution(n, c):
    dp = [0]*(n+1)
    dp[0] = 1
    for coin in c:
        for i in range(coin, n+1):
            dp[i] += dp[i-coin]
    return dp[n]


@pytest.mark.parametrize("n, c, expected", [
    (10, [2, 5, 3, 6], 5),
    (4, [1, 2, 3], 4)
])
def test_simple(n, c, expected):
    assert solution(n, c) == expected
