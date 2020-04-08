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


"""
3가지 수로 소수를 만드는 문제이다.

만들어지는 규칙을 보니 소수 1개와 소수가 아닌 수 2개로 이루어지면 소수가 만들어 지는 것 같았다.
흠 근데 아닌 경우가 있었다.

다음으로 생각한 방법

조합을 구한다
조합의 합을 구한다. set으로 중복 제거를 해준다
그 다음 set 안에서 소수를 찾고, 개수를 리턴한다.
처참하게 틀렸다. 다른 사람 풀이를 봐도 이렇게 푸는 것 같은데 왜인지 모르겠다.🧐

    from itertools import combinations


    def solution(nums):
        # 조합을 만든다
        comb = list(combinations(nums, 3))

        # 조합의 합을 구해서 set으로 만든다
        sum_comb = set(map(lambda x: sum(x), comb))

        # 소수를 sum_comb 리스트에서 빼준다
        for i in range(2, int(max(sum_comb) ** 0.5) + 1):
            # range에 인자가 3개 인 경우, 마지막 인자는 얼마씩 증가하는지를 나타낸다
            sum_comb -= set(range(i * 2, max(sum_comb) + 1, i))

        return len(sum_comb)

아 이유를 알았따!
(1,2,5), (1,3,4) 면 다른 조합이니까 합이 같아도 다른 경우로 봐야하는데, 나는 set으로 처리하면서 하나의 경우로 봐서 틀렸다.


생각을 하다가 바꾼 코드는 아래와 같았는데 3중 for문이라서 그런지 런타임 에러가 나는게 있었다.

    def solution(nums):
        # 조합을 만든다
        comb = list(combinations(nums, 3))

        # 조합의 합을 구해서 list로 만든다
        sum_comb = list(map(lambda x: sum(x), comb))
        for i in range(2, int(max(sum_comb) ** 0.5) + 1):
            for i in range(i * 2, max(sum_comb) + 1, i):
                # 리스트 안에 모든 i 삭제
                sum_comb = [x for x in sum_comb if x != i]
        return len(sum_comb)
"""
