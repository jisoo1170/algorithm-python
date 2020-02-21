import pytest
import heapq


def solution(scoville, K):
    answer = 0
    # 기존 list를 heapq로 바꾸는 방법
    heapq.heapify(scoville)
    while scoville[0] < K:
        if len(scoville) < 2:
            return -1
        answer += 1
        min1 = heapq.heappop(scoville)
        min2 = heapq.heappop(scoville)
        num = min1+min2*2
        heapq.heappush(scoville, num)
    return answer


@pytest.mark.parametrize("scoville, K, expected", [
    ([1, 2, 3, 9, 10, 12], 7, 2)
])
def test_simple(scoville, K, expected):
    assert solution(scoville, K) == expected
