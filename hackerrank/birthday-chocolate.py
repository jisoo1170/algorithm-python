def birthday(s, d, m):
    answer = 0
    for i, s1 in enumerate(s):
        s2 = s[i:m + i]
        if sum(s2) == d and len(s2) == m:
            answer += 1
    return answer
