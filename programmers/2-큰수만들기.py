import pytest


@pytest.mark.parametrize("number, k, expected", [
    ("1924", 2, "94"),
    ("1231234", 3, "3234"),
    ("4177252841", 4, "775841")
])
def test_simple(number, k, expected):
    assert solution(number, k) == expected


# 자신보다 이전에 들어온 작은 수는 모두 빼주자
# 빼는 개수 k가 0보다 작으면 그냥 합쳐주기만 하면 됨
# 만약에 k를 다 쓰지 않았다면 뒤에서 부터 k만큼 제거한다
def solution(number, k):
    answer = ''
    collected = []
    for n in number:
        while collected and collected[-1] < n and k > 0:
            collected.pop()
            k -= 1
        collected.append(n)
    if k > 0:
        collected = collected[:-k]
    answer = "".join(collected)
    return answer
