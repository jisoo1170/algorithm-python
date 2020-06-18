def timeConversion(s):
    check = s[-2:]
    s = s[:-2]
    time = s.split(":")
    if check == "PM":
        if time[0] != "12":
            time[0] = str(int(time[0]) + 12)
    else:
        if time[0] == "12":
            time[0] = "00"
    s = ":".join(time)
    return s
