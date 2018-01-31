import math
result = 0
with open('sum3.txt', 'r') as f:
    first_line = f.readline()
    rows = first_line.strip().strip(';')
    for x in range(0, int(rows)):
        for line in f:
            r, n, l = [float(x) for x in line.strip().strip(";").split(',')]

            if n == 3 and r >= math.ceil(float(l) / (3 ** 0.5)):
                result += 1
            if n == 4 and r >= math.ceil(float(l) / (2 ** 0.5)):
                result += 1
    print(result)
