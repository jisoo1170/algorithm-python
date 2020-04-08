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


"""
대박! 표를 그려보니 완전 dfs문제였다. 개념 공부를 할 때 봤던거랑 너무 똑같아서 기분이 좋았다. 캬캬캬

하 역시 구현은 어려웠다... 시간이 겁나 오래걸렸다ㅜㅅㅜ

연결되어 있는 컴퓨터는 stack에 넣어주고 방문했다고 체크를 해준다.
더이상 연결된게 없으면 stack에서 pop을 해서 그 컴퓨터에 연결된 컴퓨터를 또 쏴악 검사한다.

stack 이 완전히 빈 경우 방문하지 않은 다음 컴퓨터를 검사한다.(i)
이 경우가 연결되지 않은 경우이기 때문에 answer +1 해준다.
"""