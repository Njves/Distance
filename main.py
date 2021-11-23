def cg_distance(x1, y1, x2, y2, x3, y3, x4, y4) -> float:
    middle_side_a = (x2 + x1) / 2, (y1 + y2) / 2
    middle_side_b = (x3 + x4) / 2, (y4 + y3) / 2
    print(middle_side_a, middle_side_b)
    dist = (middle_side_b[0] - middle_side_a[0]) ** 2 + (middle_side_b[1] - middle_side_a[1]) ** 2
    return round(dist ** 0.5, 2)
