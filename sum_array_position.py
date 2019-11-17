# Amazon interview question. Find integers in order within an array whos sum equals the target.
# Print the start and end array position of these integers when found.
# This stops on first set found. Remove the if position statement to keep going until depleted


master = [1, 2, 4, 5, 6, 27, 92, 28, 75]
target = 42

working = master.copy()

length = len(working)

position = []

for x in range(0, length, 1):
    if len(position) == 0:
        work2 = working.copy()
        length2 = len(work2)
        for y in range(length2 -1, -1, -1):
            if sum(work2) == target:
                print("Found", work2)
                print("Y:", y)
                position = [x + 1, x + len(work2)]
                print("Found @", position)
                #work2.pop(y)
                break
            else:
                #print(work2)
                work2.pop(y)
        working.pop(0)
    else:
        break









