def insertion(li):
    for i in range(len(li)):
        # 현재 idx 보다 작은 idx 안(즉, 정렬된 부분)에서 값 비교
        for j in range(i):
            if li[i] < li[j]:
                li[i], li[j] = li[j], li[i]


if __name__ == "__main__":
    li = [8, 5, 6, 2, 4]
    insertion(li)
    print(li)
