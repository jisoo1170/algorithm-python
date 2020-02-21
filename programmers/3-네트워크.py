import pytest
from collections import deque


def solution(n, computers):
    answer = 0
    bfs = []
    visit = [False]*n
    for i in range(n):
        if visit[i] is True:
            continue
        bfs.append(i)
        answer += 1
        while bfs:
            now = bfs.pop()
            visit[now] = True
            for j in range(n):
                if computers[now][j] == 1 and visit[j] is False:
                    bfs.append(j)
    return answer


@pytest.mark.parametrize("n, computers, expected", [
    (3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]],	2),
    (3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]],	1)
])
def test_simple(n, computers, expected):
    assert solution(n, computers) == expected
