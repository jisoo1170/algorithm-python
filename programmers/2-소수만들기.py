import pytest
from itertools import combinations


def solution(nums):
    # 조합을 만든다
    comb = list(combinations(nums, 3))

    # 조합의 합을 구해서 set으로 만든다
    sum_comb = list(map(lambda x: sum(x), comb))
    n = set()
    # 소수를 구해서 n에 추가한다
    for i in range(2, int(max(sum_comb) ** 0.5) + 1):
        # range에 인자가 3개 인 경우, 마지막 인자는 얼마씩 증가하는지를 나타낸다
        n |= set(range(i * 2, max(sum_comb) + 1, i))
    # 소수를 sum_comb 리스트에서 빼준다
    sum_comb = [x for x in sum_comb if x not in n]
    return len(sum_comb)


@pytest.mark.parametrize("nums, expected", [
    ([1, 2, 3, 4], 1),
    ([1, 2, 7, 6, 4], 4),
    ([1, 2, 5, 3, 4], 2)
])
def test_simple(nums, expected):
    assert solution(nums) == expected
