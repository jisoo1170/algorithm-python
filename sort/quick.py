# pivot을 기준으로 작은 값은 왼쪽에 큰 값은 오른쪽에
# 재귀로 반복!


def quick(li):
    if len(li) < 2:
        return li
    pivot = li[len(li)//2]
    print(li, pivot)
    left = []
    right = []
    for l in li:
        if l < pivot:
            left.append(l)
        elif l > pivot:
            right.append(l)
    left = quick(left)
    right = quick(right)
    return left+[pivot]+right


if __name__ == "__main__":
    li = [8, 5, 6, 2, 4, 1, 3, 9]
    print(quick(li))
