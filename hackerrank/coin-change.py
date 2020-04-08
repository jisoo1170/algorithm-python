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


"""
저번에 백준에서 풀었던 문제와 동일하다.
근데 왜 이렇게 모르겠짘ㅋㅋㅋ 하

알고리즘 문제들 나중에 보면 다 모를 것 같다... 꾸준히 공부해야지ㅜ

내가 생각한 풀이 방법은!

만약 동전 1, 2, 3을 가지고 4를 구한다고 하면 dp[4] = dp[4-1] + dp[4-2] + dp[4-3]
이런 점화식으로 구할 수 있을 거라고 생각했다.
이유는 3에 1을 더하면 4고, 2에 2를 더하면 4, 1에 3을 더하면 4니까!

그런데 문제는 중복이 생긴다는 것이다.
다른 풀이를 보며 이해하니 완전 잘못 접근했다.

for문을 돌면서 1, 2, 3으로 만들 수 있는 가짓수를 더해준다.

    # 동전이 1인 경우
    dp[1] += dp[1-1]
    dp[2] += dp[2-1]
    dp[3] += dp[3-1]
    dp[4] += dp[4-1]

    # 동전이 2인 경우
    dp[2] += dp[2-2]
    dp[3] += dp[3-2]
    dp[4] += dp[4-2]

    # 동전이 3인 경우
    dp[3] += dp[3-3]
    dp[4] += dp[4-3]

이렇게 될 것이다.

코드로 구현하면 아래와 같다.
"""
