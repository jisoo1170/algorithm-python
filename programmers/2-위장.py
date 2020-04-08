import pytest


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


"""
조합은 맞았으나 더 간단하게 생각하면 풀리는 문제였다.
우선 해시를 만들어서 같은 키를 가지는 value를 넣어준다.
(value, key)의 형태로 들어오니까 (1,1), (2,1)가 들어온다고 생각하면, 해쉬 맵은 {1 : [1, 2]}가 된다.

그 다음 묶어진 value들끼리 조합을 만들어준다. 간단하게 value 개수를 곱해주면 된다.
여기서 주의해야 할 점은 한 카테고리에서 선택을 안하는 경우도 넣어 줘야 하기 때문에, +1을 한 상태에서 곱해준다.
이렇게 되면 모든 카테고리에서 선택을 안하는 경우가 나오기 때문에 정답에서 -1을 해서 그 경우를 빼준다.

처음에 작성한 코드
    def solution(clothes):
        answer = 1
        hash_map = dict()

        for value, key in clothes:
            if key not in hash_map.keys():
                hash_map.setdefault(key, [])
            hash_map[key].append(value)
        print(hash_map)
        for i in hash_map.values():
            answer *= (len(i)+1)
        return answer

안 좋은 점은 배열에 값을 넣고 그 길이를 구한다는 것이다.
다른 사람 코드 처럼 아예 수를 넣어주는게 더 효율적일 것 같다.
"""
