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
