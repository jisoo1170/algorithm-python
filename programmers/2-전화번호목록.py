import pytest


@pytest.mark.parametrize("phone_book, expected", [
    ([119, 97674223, 1195524421], False),
    ([123, 456, 789], True),
    ([12, 567, 88, 13125], True)
])
def test_simple(phone_book, expected):
    assert solution(phone_book) == expected


# 문자열로 바꿔서 정렬하면 무조건 비슷한 수가 근처에 오니까 앞 뒤만 비교해도 된다
def solution(phone_book):
    answer = True
    phone_book = list(map(str, phone_book))
    phone_book.sort()
    for p1, p2 in zip(phone_book, phone_book[1:]):
        if p2.startswith(p1):
            return False

    return answer


if __name__ == "__main__":
    solution(input)
