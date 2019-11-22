input_array = [1, 2, 4, 5, 6, 27, 92, 14, 28, 75]
target = 42


def sum_array_pos(target, input_array):
    x = 0
    y = 0
    while y <= len(input_array) and x <= len(input_array):
        if sum(input_array[x:y]) == target:
            print(input_array[x:y])
            print("Position: ", x + 1)
        elif sum(input_array[x:y + 1]) > target:
            #remove this elif statement if input_array can contain negative numbers
            x += 1
            y = x
        y += 1
        if y == len(input_array) + 1:
            x += 1
            y = x

sum_array_pos(target, input_array)