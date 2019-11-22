master = [1, 2, 4, 5, 6, 27, 92, 14, 28, 75]
target = 42

x = 0
y = 0

while y <= len(master) and x <= len(master):
    if sum(master[x:y]) == target:
        print(master[x:y])
        print("Position: ", x + 1)
    elif sum(master[x:y + 1]) > target:
        x += 1
        y = x
    y += 1
    if y == len(master) + 1:
        x += 1
        y = x