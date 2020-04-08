import pytest


def solution(numbers, target):
    global answer
    answer = 0
    global len_num
    len_num = len(numbers)-1
    global t
    t = target
    drf(numbers, 0)
    return answer


def drf(numbers, idx):
    print(numbers)
    if idx > len_num:
        if sum(numbers) == t:
            print("rk")
            global answer
            answer += 1
        return
    else:
        drf(numbers, idx+1)
        numbers[idx] *= -1
        drf(numbers, idx+1)


@pytest.mark.parametrize("numbers, target, expected", [
    ([1, 1, 1, 1, 1], 3, 5),
    ([1, 2, 3], 0, 2)
])
def test_simple(numbers, target, expected):
    assert solution(numbers, target) == expected


"""
재귀호출을 이용해서 구현했다.
사실 이것도 처음에는 어떻게 풀어야하는지 감이 안왔다.

역시 풀이는 생각보다 쉬웠다.

곱하기1 인 경우와 곱하기-1 인 경우를 나눠서 재귀호출을 계속 돌면 됐다.
재귀를 돌다가 idx가 마지막에 오면 numbers의 합을 계산한다.
그 합이 target과 같으면 answer에 1을 더해주고 retrun 한다.
"""
