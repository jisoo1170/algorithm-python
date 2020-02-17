import pytest
from collections import deque


@pytest.mark.parametrize("bridge_length, weight, truck_weights, expected", [
    (2,	10,	[7, 4, 5, 6], 8),
    (100, 100, [10], 101),
    (100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10], 110)
])
def test_simple(bridge_length, weight, truck_weights, expected):
    assert solution(bridge_length, weight, truck_weights) == expected


def solution(bridge_length, weight, truck_weights):
    answer = 0
    truck_weights.reverse()
    current_weight = 0
    truck_on_birdge = deque([0]*bridge_length, maxlen=bridge_length)
    while truck_weights:
        answer += 1
        # 다리 위에서 빠지는 값을 체크해서 현재 무게에서 빼준다
        finish = truck_on_birdge.popleft()
        current_weight -= finish
        # 다리무게 >= 현재무게 인 경우 트럭을 넣어준다
        if current_weight+truck_weights[-1] <= weight:
            now = truck_weights.pop()
            finish = truck_on_birdge.append(now)
            current_weight += now
        # 그게 아닌 경우 0을 넣어준다
        else:
            finsih = truck_on_birdge.append(0)
    # 다리 위에 놓여진 트럭을 다 밀어주고 끝낸다
    while truck_on_birdge:
        answer += 1
        truck_on_birdge.pop()
    return answer


if __name__ == "__main__":
    solution(input)
