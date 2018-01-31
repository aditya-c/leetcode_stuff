def count_drops(distribution):
    total = 0
    max_location = distribution.index(max(distribution))

    # from left to max
    curr_max = 0
    for loc in range(max_location + 1):
        curr_max = max(curr_max, distribution[loc])
        total += curr_max - distribution[loc]

    # form right to max
    curr_max = 0
    for loc in reversed(range(max_location, len(distribution))):
        curr_max = max(curr_max, distribution[loc])
        total += curr_max - distribution[loc]

    return total


print(count_drops([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
print(count_drops([3, 1, 3]))
