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


"""
큐를 이용해서 풀었다.

먼저 각 기능의 배포 날짜를 계산하고, 한 번에 몇개가 가능한지 구해준다.
한번에 가능한 갯수는 뒤에 더 큰 값이 나오기 전까지다.


다른 사람의 풀이를 보니 max 변수를 따로 지정하지 않고 앞 뒤 값을 비교해도 됐을 것 같다.

if daysLeft[i] < daysLeft[i + 1]:
    retList.append(count)
    count = 1
else:
    daysLeft[i + 1] = daysLeft[i]
    count += 1
"""
