def gradingStudents(grades):
    answer = []
    for g in grades:
        temp = 5 - g % 5
        if temp < 3:
            if g + temp < 40:
                answer.append(g)
            else:
                answer.append(g + temp)
        else:
            answer.append(g)
    return answer
