def longest_increasing_subsequence(d):
    'Return one of the L.I.S. of list d'
    l = []
    for i in range(len(d)):
        l.append(max([l[j] for j in range(i) if l[j][-1] < d[i]] or [[]], key=len)
                 + [d[i]])
        # print(i, [l[j] for j in range(i) if l[j][-1] < d[i]] or [[]], l)
        print(l)
    return max(l, key=len)


# def lbs(arr):
#     n = len(arr)

#     # allocate memory for LIS[] and initialize LIS values as 1
#     # for all indexes
#     lis = [1 for i in range(n + 1)]

#     # Compute LIS values from left to right
#     for i in range(1, n):
#         for j in range(0, i):
#             if ((arr[i] > arr[j]) and (lis[i] < lis[j] + 1)):
#                 lis[i] = lis[j] + 1
#     return max(lis)


if __name__ == '__main__':
    for d in [[3, 2, 6, 3, 4, 5, 1], [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]]:
        print('a L.I.S. of %s is %s' % (d, longest_increasing_subsequence(d)))
    # print(lbs([3, 2, 6, 3, 4, 5, 1]))
