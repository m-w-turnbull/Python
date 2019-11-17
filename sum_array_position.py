# Amazon interview question. Find integers in order within an array whos sum equals the target.
# Print the start and end array position of these integers when found.


master = [1, 2, 4, 5, 6, 27, 92]
target = 15

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
                position = [x + 1, len(master) - y]
                print("Found @", position)
                #work2.pop(y)
                break
            else:
                #print(work2)
                work2.pop(y)
        working.pop(0)
    else:
        break









