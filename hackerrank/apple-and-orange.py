def countApplesAndOranges(s, t, a, b, apples, oranges):
    apple = [a + t for t in apples]
    orange = [b + t for t in oranges]
    answer = [0, 0]
    for app in apple:
        if app >= s and app <= t:
            answer[0] += 1
    for ora in orange:
        if ora >= s and ora <= t:
            answer[1] += 1
    print(answer[0])
    print(answer[1])
