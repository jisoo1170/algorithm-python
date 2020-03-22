# 분할하고 합치는 과정에서 정렬이 일어난다
def divide(li):
    if len(li) < 2:
        return li
    mid = len(li)//2
    left = divide(li[:mid])
    right = divide(li[mid:])
    # print(left, right, "divide-")
    return merge(left, right)


def merge(left, right):
    result = []
    # print(left, right, "merge---")
    while len(left) > 0 and len(right) > 0:
        if left[0] > right[0]:
            result.append(right[0])
            right = right[1:]
        else:
            result.append(left[0])
            left = left[1:]
    if len(left) > 0:
        result += left
    if len(right) > 0:
        result += right
    # print(result, "result-------")
    return result


if __name__ == "__main__":
    li = [8, 5, 6, 2, 4, 1, 3, 9]
    print(divide(li))
