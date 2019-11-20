rectangle1 = ([1, 2], [5, 5])
rectangle2 = ([3, 3], [7, 8])

#create all points in rectangle

def rectangle_points(coordinate_set):
    all_coords = []
    for x in range(int(coordinate_set[0][0]), int(coordinate_set[1][0]) + 1):
        for y in range(int(coordinate_set[0][1]), int(coordinate_set[1][1]) + 1):
            all_coords.append([x, y])
    return all_coords

def compare_coords(rec1, rec2):
    same_coords = []
    for i in rec1:
        if i in rec2:
            same_coords.append(i)
    return same_coords

def define_common_rectangle(coordinates):
    common_rectangle = (coordinates[0], coordinates[-1])
    return common_rectangle

rec1_coords = rectangle_points(rectangle1)
rec2_coords = rectangle_points(rectangle2)

same_coords = compare_coords(rec1_coords, rec2_coords)

#print(same_coords[0], same_coords[-1])
print(define_common_rectangle(same_coords))
