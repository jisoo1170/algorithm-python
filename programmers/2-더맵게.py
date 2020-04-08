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


"""
python의 heapq 라이브러리를 이용해서 아주 아주 간단하게 풀었다.
최소힙을 구현해 놓은 것으로 자동으로 계속 정렬을 해준다.

heapq 리스트에서 첫 번째와 두 번째 값을 꺼내서 계산 한 다음, 다시 리스트에 넣어주면 된다.

while문이 멈추는 때는 heapq의 처음 값이 K랑 같거나 클 때이다.
"""
