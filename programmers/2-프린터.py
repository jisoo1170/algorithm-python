import pytest
from collections import deque


def solution(priorities, location):
    p_list = deque((value, idx) for idx, value in enumerate(priorities))
    print(p_list)
    priorities.sort(reverse=True)
    idx = 0
    done = []
    while True:
        p = p_list.popleft()
        if len(p_list) == 0:
            done.append(p)
            break
        if priorities[idx] == p[0]:
            done.append(p)
            idx += 1
        else:
            p_list.append(p)

    for i, item in enumerate(done):
        if item[1] == location:
            return i+1


@pytest.mark.parametrize("priorities, location, expected", [
    ([2, 1, 3, 2], 2, 1),
    ([1, 1, 9, 1, 1, 1], 0, 5)
])
def test_simple(priorities, location, expected):
    assert solution(priorities, location) == expected


"""
큐로 생각해서 넣고 빼주면 되겠다고 생각했다.

그런데 자신보다 뒤에 큰 수가 있으면 리스트 뒤로 다시 넣어줘야 하는데 이 부분을 어떻게 해야하는지 막막했고,
리스트가 계속 변하는데 처음 인덱스를 어떻게 가지고서 location 과 비교해야 하는지 막막했다.
내가 바로 알린이

생각보다 간단했다!

p_list라는 큐를 만들고 priorites의 인덱스와 함께 저장한다.
그 다음 priorites를 정렬해서 내림차순으로 만들어준다. 최댓값을 순서대로 확인하기 위해서다. 그 순서는 idx로 체크했다.

pirorites[idx] 즉, 현재 최댓값과 p_list 제일 앞의 값을 비교해서 그 값이 같으면 출력 완료 리스트에 넣어준다.(done)
그렇지 않다면 p_list 제일 뒤에 넣어주면 된다.

처음에는 list를 사용해서 reverse해서 pop()시간을 줄이려고 했는데, 그냥 deque를 활용하면 될 일이였다.
"""
