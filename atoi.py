def myAtoi(str):
    i = 0
    str1 = str.strip()
    try:
        for x in range(0, len(str1)):
            if x == 0 and (str1[0] == "+" or str1[0] == "-"):
                continue
            i = int(str1[:x + 1])

    except Exception as e:
        return output(i)
    return output(i)


def output(i):
    if i > 2147483647:
        return 2147483647
    if i < -2147483648:
        return -2147483648
    return i


print(myAtoi("      -11919730356x"))
