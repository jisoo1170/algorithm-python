import pytest
from collections import deque


def solution(priorities, location):
    p_list = deque((value, idx) for idx, value in enumerate(priorities))
    print(p_list)
    priorities.sort(reverse=True)
    idx = 0
    done = []
    while True:
        p = p_list.popleft()
        if len(p_list) == 0:
            done.append(p)
            break
        if priorities[idx] == p[0]:
            done.append(p)
            idx += 1
        else:
            p_list.append(p)

    for i, item in enumerate(done):
        if item[1] == location:
            return i+1


@pytest.mark.parametrize("priorities, location, expected", [
    ([2, 1, 3, 2], 2, 1),
    ([1, 1, 9, 1, 1, 1], 0, 5)
])
def test_simple(priorities, location, expected):
    assert solution(priorities, location) == expected
