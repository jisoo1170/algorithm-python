import pytest


# def solution(clothes):
#     answer = 1
#     hash_map = dict()

#     for value, key in clothes:
#         if key not in hash_map.keys():
#             hash_map.setdefault(key, [])
#         hash_map[key].append(value)
#     print(hash_map)
#     for i in hash_map.values():
#         answer *= (len(i)+1)
#     return answer

def solution(clothes):
    clothes_type = {}

    for c, t in clothes:
        if t not in clothes_type:
            clothes_type[t] = 1
        clothes_type[t] += 1

    cnt = 1
    for num in clothes_type.values():
        cnt *= num

    return cnt - 1


@pytest.mark.parametrize("clothes, expected", [
    ([['yellow_hat', 'headgear'], ['blue_sunglasses', 'eyewear'],
     ['green_turban', 'headgear']], 5),
    ([['crow_mask', 'face'], ['blue_sunglasses', 'face'],
     ['smoky_makeup', 'face']], 3)
])
def test_simple(clothes, expected):
    assert solution(clothes) == expected


if __name__ == "__main__":
    solution(input)
