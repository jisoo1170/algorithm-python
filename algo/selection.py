def selection(li):
    # 정렬되지 않은 부분 중 가장 작은 값을 정렬된 부분 끝에 추가
    for i in range(len(li)-1):
        min_idx = -1
        min = li[i]
        # 최솟값을 찾는 for문
        for j in range(i, len(li)-1):
            if min > li[j]:
                min = li[j]
                min_idx = j
        # 최솟값을 정렬된 뒷부분에 추가
        li[i], li[min_idx] = li[min_idx], li[i]
        print(li, i, min_idx)


if __name__ == "__main__":
    li = [8, 5, 6, 2, 4]
    selection(li)
    print(li)
