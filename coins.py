def count(n):
    print(n, "---")
    # If n is 0 then there is 1 solution(do not include any coin)
    if (n == 0):
        return True

     # If n is less than 0 then no solution exists
    if (n < 0):
        return False

     # If there are no coins and n is greater than 0, then no solution exist
    # if (m <= 0 and n >= 1):
    #     return 0

     # count is sum of solutions(i) including S[m - 1](ii) excluding S[m - 1]
    return count(n - 10) or count(n - 2) or count(n - 3)


# Driver program to test above function
arr = [1, 2, 3]
print(count(1))
