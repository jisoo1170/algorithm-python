import pytest


def solution(s):
    stack = []
    for i in s:
        if i == '(':
            stack.append(0)
        else:
            if len(stack) < 1:
                return False
            stack.pop()

    return len(stack) == 0


@pytest.mark.parametrize("s, expected", [
    # ("()()", True),
    ("(())()", True)
    # (")()(", False),
    # ("(()(", False)
])
def test_simple(s, expected):
    assert solution(s) == expected


if __name__ == "__main__":
    solution(input)

"""
'()'를 지워가면서 이전 lenght와 비교해서 변화가 없으면 괄호가 올바르지 않을 것이라고 생각했다.
근데 효율성 부분에서 시간초과가 났다
replace 는 문자열을 복사해서 가공하기 때문!!

    def solution(s):
        answer = True
        before_length = 0
        while len(s) != before_length:
            before_length = len(s)
            s = s.replace('()', '')
        if before_length > 0:
            return False
        return True

간지나게 풀려고 했으나 정석이 좋았다
"""
