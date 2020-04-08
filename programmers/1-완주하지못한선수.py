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


"""
처음 한 생각은 for문을 돌면서 값을 비교하고 같은 값을 가지는 경우에는 remove를 해주면 될 것 같았다.
그런데 효율성 테스트 부분에서 시간 초과가 발생했다. remove가 o(n)의 시간 복잡도를 가지기 때문!!

    def solution(participant, completion):
        for c in completion:
            for p in participant:
                if c == p:
                    participant.remove(p)
                    break
        return participant.pop()
        
그래서 저 remove부분을 어떻게 하면 좋을까 생각하다가 set이 해쉬함수로 이루어져있다는 것이 생각났다. 면접에서 얻은 지식ㅋㅋㅋㅋ


    def solution(participant, completion):
        answer = set(participant) - set(completion)
        return answer.pop()

이렇게 수정하였는데 participant 는 중복을 허용한다고 하여 오류가 발생했다. 문제를 잘 읽읍시다!!

아무튼 그래서 Counter라는 객체를 사용했다. Counter는 같은 키를 가지는 value의 개수를 세주는 것이다.
이것은 뺄셈을 할 수 있는데 그러면 자연스럽게 다른 1개만 남을 것이고 그 키 값을 받아오면 된다.
{'key': 1} 이런 형태임
"""
