def decodeNumber(s):
    if not s:
        return 0
    prev, curr, prev_value = 0, 1, ""
    print(prev, curr, prev_value)
    for digit in s:
        prev, curr, prev_value = curr, (digit > '0') * curr + int(10 <= int(prev_value + digit) <= 26) * prev, digit
    return curr


print("*" * 10)
print(decodeNumber("1234"))
