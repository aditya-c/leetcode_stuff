with open('sum4.txt', 'r') as f:
    array = []
    for line in f:
        input_array = [int(x) for x in line.strip().split()]
        result_array = []
        result_array[0] = input_array[0]
        for x in range(1, len(input_array)):
            if input_array[x - 1] == 1:
                result_array[x] = 1


# main_arr = []
# for x in range(0, 3):
#     inp = input()
#     arr = list(inp.split())
#     main_arr.append(arr)

transpose = [list(i) for i in zip(*array)]

for item in transpose:
    print(' '.join(map(str, item)))
