import pytest
from itertools import permutations


def solution(n):
    a = set()
    for i in range(len(n)):
        a |= set(map(int, map("".join, permutations(list(n), i + 1))))
    a -= set(range(0, 2))
    print(max(a))
    print(max(a) ** 0.5)
    for i in range(2, int(max(a) ** 0.5) + 1):
        print(i)
        a -= set(range(i * 2, max(a) + 1, i))
    return 0


@pytest.mark.parametrize("numbers, expected", [
    # ("17", 3),
    ("011", 2)
])
def test_simple(numbers, expected):
    assert solution(numbers) == expected


"""
수를 어떻게 조합해야 하나 모르겠어서 겁나 삽질했는데 검색해보니 파이썬에는 순열을 만들어주는 함수가 있었다.

import itertools

itertools.permutations(numbers, length)
여기서 length는 순열의 길이를 지정하는,,


처음에 내가 짠 코드

    def check_prime(arr, length):
        sum = 0
        arr = set(map(int, arr))
        check = [False]*2+[True]*(max(arr)-1)
        for a in arr:
            if check[a] is False or len(str(a)) < length:
                continue
            for i in range(2, a+1):
                for j in range(2, (a//i)+1):
                    check[i*j] = False
            if check[a] is True:
                print(a)
                sum += 1
        return sum

solution 에서 permutations 함수를 이용해서 순열을 구해주고 set으로 중복을 제거해줬다.
소수를 체크하는 부분에서 시간이 너무 오래 걸린다. 무려 for문을 3번..!!!!


정답 코드는 진짜 빠르고 좋았다,,,
저기 set(range(i * 2, max(a) + 1, i)) 이 부분을 출력해보면
    {4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32,
        34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60,
        62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88,
        90, 92, 94, 96, 98, 100, 102, 104, 106, 108, 110}
이런 식으로 나오는데 진짜 대박인 것 같다

range 함수는 인자로 (시작, 끝, 숫자 사이 거리) 를 넣을 수 있다.
for문 범위를 max(a)의 0.5제곱으로 하는 이유는 range에서 i 단위로 더해지기 때문에 미리 막아서 제어하는?

예를 들어 max(a)가 110 이면 max(a)**0.5 는 10.어쩌구

그러면 range 는 {20, 30, 40, 50, 60, 70, 80, 90, 100, 110} 이 되기 때문!

n이 소수인지 체크한다 -> 2~루트n 범위까지만 돌면서 n이 나누어 떨어지는지 확인하면 된다.
"""
