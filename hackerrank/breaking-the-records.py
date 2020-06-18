def breakingRecords(scores):
    max_count = 0
    min_count = 0

    max_num = scores[0]
    min_num = scores[0]

    for s in scores:
        if s < min_num:
            min_count += 1
            min_num = s
        if s > max_num:
            max_count += 1
            max_num = s
    return [max_count, min_count]
