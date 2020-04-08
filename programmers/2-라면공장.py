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


"""
어떻게 접근해야 하는지 감이 안왔다. 다른 분의 풀이를 참고했다.

stock을 빼지 않고 버틸 수 있는 날 안에서 가장 많은 물량을 가진 날을 선택하는 방법이다.
그러다가 stock이 정상 공급을 받을 수 있는 날인 K보다 같거나 커지면 종료하면 된다.

풀이 방법
stock이 k보다 작은 경우 반복한다.
stock 보다 작거나 같은 날짜를 확인한다.
그 중에서 가장 많은 양을 재공할 수 있는 날짜를 선택한다.
= 큐에 날짜에 해당하는 재고를 넣고 가장 큰 값을 뽑아낸다.
"""
