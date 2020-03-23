def insertion(li):
    for i in range(1, len(li)):
        # 현재 idx 보다 작은 idx 안(즉, 정렬된 부분)에서 값 비교
        for j in range(i, 0, -1):
            print(j, li)
            if li[j] > li[j-1]:
                break
            li[j], li[j-1] = li[j-1], li[j]
            print(j, li, '------')


if __name__ == "__main__":
    li = [8, 5, 6, 2, 4]
    insertion(li)
    print(li)
