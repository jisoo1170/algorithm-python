import pytest
from collections import Counter


def solution(participant, completion):
    answer = Counter(participant) - Counter(completion)
    return list(answer.keys()).pop()


@pytest.mark.parametrize("participant, completion, expected", [
    (["eden", "kiki", "eden"], ["eden", "kiki"], "eden"),
    (["marina", "josipa", "nikola", "vinko", "filipa"],
        ["josipa", "filipa", 'marina', 'nikola'], 'vinko')
])
def test_simple(participant, completion, expected):
    assert solution(participant, completion) == expected
