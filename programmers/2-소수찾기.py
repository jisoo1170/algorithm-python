import pytest
from itertools import permutations


@pytest.mark.parametrize("numbers, expected", [
    # ("17", 3),
    ("011", 2)
])
def test_simple(numbers, expected):
    assert solution(numbers) == expected


# def check_prime(arr, length):
#     sum = 0
#     arr = set(map(int, arr))
#     check = [False]*2+[True]*(max(arr)-1)
#     for a in arr:
#         if check[a] is False or len(str(a)) < length:
#             continue
#         for i in range(2, a+1):
#             for j in range(2, (a//i)+1):
#                 check[i*j] = False
#         if check[a] is True:
#             print(a)
#             sum += 1
#     return sum


# def solution(numbers):
#     answer = 0
#     for i in range(1, len(numbers)+1):
#         num_list = set(map(''.join, permutations(numbers, i)))
#         answer += check_prime(num_list, i)
#     return answer


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


if __name__ == "__main__":
    solution(input)
