coord_set1 = [[-3, -2], [1, 2]]
coord_set2 = [[-5, 1], [-2, 5]]

def find_maxes(coord1, coord2):
    x1 = coord1[0]
    x2 = coord2[0]
    if x1 >= x2:
        maxx = x1
    else:
        maxx = x2
    y1 = coord1[1]
    y2 = coord2[1]
    if y1 >= y2:
        maxy = y1
    else:
        maxy = y2
    return(maxx, maxy)

def find_mins(coord1, coord2):
    x1 = coord1[0]
    x2 = coord2[0]
    y1 = coord1[1]
    y2 = coord2[1]
    if x1 <= x2:
        minx = x1
    else:
        minx = x2
    if y1 <= y2:
        miny = y1
    else:
        miny = y2
    return(minx, miny)



overlap = []
overlap.append(find_maxes(coord_set1[0], coord_set2[0]))
overlap.append(find_mins(coord_set1[1], coord_set2[1]))
print(overlap)


