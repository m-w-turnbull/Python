coord_set1 = [[-3, -2], [1, 2]]
coord_set2 = [[-5, 1], [-2, 5]]

def find_maxes(coord1, coord2):
    maxx = []
    maxx.append(coord1[0])
    maxx.append(coord2[0])
    maxx = max(maxx)
    maxy = []
    maxy.append(coord1[1])
    maxy.append(coord2[1])
    maxy = max(maxy)
    return(maxx, maxy)

def find_mins(coord1, coord2):
    minx = []
    miny = []
    minx.append(coord1[0])
    minx.append(coord2[0])
    miny.append(coord1[1])
    miny.append(coord2[1])
    minx = min(minx)
    miny = min(miny)
    return(minx, miny)

def find_the_overlap(coordset1, coordset2):
    overlap = []
    overlap.append(find_maxes(coordset1[0], coordset2[0]))
    overlap.append(find_mins(coordset1[1], coordset2[1]))
    return overlap

def find_the_area_of_overlap(overlap_coords):
    overlapx = overlap[0][0] - overlap[1][0]
    overlapy = overlap[0][1] - overlap[1][1]
    area_of_overlap = overlapx * overlapy
    return area_of_overlap




overlap = find_the_overlap(coord_set1, coord_set2)
print("The area of the overlap is:", find_the_area_of_overlap(overlap))
print("The coordinates of the overlap are:", overlap)