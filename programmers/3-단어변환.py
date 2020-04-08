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


"""
내가 생각한 풀이 방법
- 바꿀 수 있는 단어를 찾는다.
- 탐색 횟수를 +1 한다.
- 기준이 되는 단어를 바꿔준다.
- 기준이 되는 단어가 target이면 반복을 멈춘다.

앗 그냥 이렇게만 작성했더니 결과가 아래처럼 나왔다.
hot
dot
dog
log
lot

BFS 개념을 적용해서 큐에 담았다. 아래와 같은 순서로 큐에 담겨져 있었다.
[hot] - [dot, lot] - [lot, dog] - [dog, log] - [log, cog] - [cog]

아래와 같은 결과가 나오게 수정했다.
while 문을 돌면서 큐의 모든 원소에 대해서 1글자 차이나는 단어를 temp 리스트에 넣어준다.
while문이 끝나면 큐에 추가해 주게 했다.
[hot] - [dot, hot] - [dog, log] - [cog]

그랬더니 성공!! 꺅
"""
