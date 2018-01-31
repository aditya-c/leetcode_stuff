def isNumber(s):
    try:
        float(x.strip())
    except Exception as e:
        return False
    else:
        return True


print(isNumber("0"))
print(isNumber(" 0.1 "))
print(isNumber("abc"))
print(isNumber("1 a"))
print(isNumber("2e10"))
