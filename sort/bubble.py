def bubble(li):
    for i in range(len(li)-1):
        for j in range(len(li)-1-i):
            # 양 옆에 값 비교
            if li[j] > li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]


if __name__ == "__main__":
    li = [8, 5, 6, 2, 4]
    bubble(li)
    print(li)
