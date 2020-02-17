import pytest


@pytest.mark.parametrize("arrangement, expected", [
    ("()(((()())(())()))(())", 17)
])
def test_simple(arrangement, expected):
    assert solution(arrangement) == expected


# 괄호가 ( 모양이면 넣어주고 ) 모양이면 빼주고 남은 개수 더하기
# 바로 () 이렇게 되는 거면 스택 개수를 넣어주고 아닌 경우는 그냥 막대가 끝났다는 의미니까 1을 더해준다
def solution(arrangement):
    answer = 0
    # stack에 남은 개수 체크
    count = 0
    check = False
    for token in arrangement:
        if token == '(':
            count += 1
            check = True
        else:
            count -= 1
            if check is True:
                answer += count
            else:
                answer += 1
            check = False

    return answer

# 아예 이렇게 () 이 문자열을 치환해서 하는 것도 더 쉽고 대박인 것 같다
# def solution(arrangement):
#     answer = 0
#     sticks = 0
#     rasor_to_zero = arrangement.replace('()','0')

#     for i in rasor_to_zero:
#         if i == '(':
#             sticks += 1
#         elif i =='0' :
#             answer += sticks
#         else :
#             sticks -= 1
#             answer += 1

#     return answer


if __name__ == "__main__":
    solution(input)
