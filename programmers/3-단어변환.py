import pytest
from collections import deque


def compare(w1, w2):
    check = 0
    for x, y in zip(w1, w2):
        if x != y:
            check += 1
    if check == 1:
        return True
    return False


def solution(begin, target, words):
    if target not in words:
        return 0
    answer = 0
    dfs = [begin]
    while target not in dfs:
        temp = []
        while dfs:
            begin = dfs.pop()
            # 문자 체크
            for w2 in words:
                if compare(begin, w2):
                    words.remove(w2)
                    temp.append(w2)
                    print(begin, dfs)
        dfs = temp
        answer += 1
    return answer


@pytest.mark.parametrize("begin, target, words, expected", [
    ("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"], 4),
    ("hit", "cog", ["hot", "dot", "dog", "lot", "log"], 0),
    ("hit", "hhh", ["hhh", "hht"], 2)
])
def test_simple(begin, target, words, expected):
    assert solution(begin, target, words) == expected
