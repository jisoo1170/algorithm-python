import pytest
import heapq


def solution(stock, dates, supplies, k):
    answer = 0
    idx = 0
    heap = []

    while stock < k:
        for i in range(idx, len(dates)):
            if dates[i] > stock:
                break
            heapq.heappush(heap, -supplies[i])
            idx = i + 1
        stock += (heapq.heappop(heap) * -1)
        answer += 1
    return answer


@pytest.mark.parametrize("stock, dates, supplies, k, expected", [
    (4, [4, 10, 15], [20, 5, 10], 30, 2)
])
def test_simple(stock, dates, supplies, k, expected):
    assert solution(stock, dates, supplies, k) == expected
