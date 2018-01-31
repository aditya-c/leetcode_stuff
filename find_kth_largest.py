def partition(numbers, left, right):
    # pivot is the rightmost element
    high = left
    while left < right:
        if numbers[left] > numbers[right]:
            numbers[left], numbers[high] = numbers[high], numbers[left]
            high += 1
        left += 1
    numbers[right], numbers[high] = numbers[high], numbers[right]
    return high


def get_kth_largest(numbers, k):
    if numbers:
        position = partition(numbers, 0, len(numbers) - 1)
        print(numbers, k, position)
        print("*" * 4)
        if k < position + 1:
            return get_kth_largest(numbers[:position], k)
        elif k > position + 1:
            return get_kth_largest(numbers[position + 1:], k - position - 1)
        else:
            return numbers[position]


test_array = [3, 1, 2, 4]
k = 2
print(sorted(test_array, reverse=True)[k - 1])
print("-" * 20)
print(get_kth_largest(test_array, k))


# print("+" * 24)


# def partition2(nums, l, r):
#     print(nums)
#     low = l
#     while l < r:
#         if nums[l] < nums[r]:
#             nums[l], nums[low] = nums[low], nums[l]
#             low += 1
#         l += 1

#     print(nums)
#     nums[low], nums[r] = nums[r], nums[low]
#     print(nums)
#     return low


# print(partition2([2, 1, 4, 3, 2, 1], 0, 5))
# print(partition([2, 1, 4, 8, 6, 7], 0, 5))
