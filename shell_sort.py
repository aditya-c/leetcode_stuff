# Python program for implementation of Shell Sort


def shellSort(arr):

    # Start with a big gap, then reduce the gap
    n = len(arr)
    gap = n // 2

    # Do a gapped insertion sort for this gap size.
    # The first gap elements a[0..gap-1] are already in gapped
    # order keep adding one more element until the entire array
    # is gap sorted
    while gap > 0:
        print("gap", gap, arr)
        for i in range(gap, n):

            # add a[i] to the elements that have been gap sorted
            # save a[i] in temp and make a hole at position i
            temp = arr[i]

            # shift earlier gap-sorted elements up until the correct
            # location for a[i] is found
            j = i
            print("temp-", temp)
            while j >= gap and arr[j - gap] > temp:
                print("j", j, "-", arr[j - gap])
                arr[j] = arr[j - gap]
                j -= gap
            # put temp (the original a[i]) in its correct location
            arr[j] = temp
        gap //= 2


# Driver code to test above
arr = [8, 7, 6, 1, 2, 3, 5]

n = len(arr)
print ("Array before sorting:")
print(arr)

shellSort(arr)

print ("\nArray after sorting:")
print(arr)