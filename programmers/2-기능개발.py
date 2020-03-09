import pytest
from collections import deque
import math


def solution(progresses, speeds):
    answer = []
    done = deque([])
    # 각 기능의 배포 날짜 계산
    for idx, progresse in enumerate(progresses):
        done.append(math.ceil((100-progresse)/speeds[idx]))
    # 배포가 한번에 몇개가 가능한지 계산
    # 현재 max보다 작으면 count를 +1 해주고 아닌 경우 answer에 넣어준다.
    max = done[0]
    count = 0
    for d in done:
        if max < d:
            answer.append(count)
            max = d
            count = 1
        else:
            count += 1
    answer.append(count)
    return answer


@pytest.mark.parametrize("progresses, speeds, expected", [
    ([93, 30, 55], [1, 30, 5], [2, 1])
])
def test_simple(progresses, speeds, expected):
    assert solution(progresses, speeds) == expected
