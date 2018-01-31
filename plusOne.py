def plusOne(A):
    Ax = list(A)
    overhead = 1
    for index in range(len(Ax) - 1, -1, -1):
        if overhead:
            temp = Ax[index] + 1
            overhead = temp // 10
            Ax[index] = temp % 10
    if overhead:
        Ax.insert(0, 1)

    for x in range(len(Ax)):
        if Ax[x] != 0:
            break
    return int("".join(map(str, Ax[x:])))


print(plusOne([0]))
