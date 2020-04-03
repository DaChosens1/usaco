def distance_between_two_points(point1, point2):
    return abs(point2[0] - point1[0]) + abs(point2[1] - point1[1])


def find_dist(points):
    last_point = points[0]
    dist = 0
    for x, y in points:
        dist += distance_between_two_points(last_point, [x, y])
        last_point = [x, y]
    return dist


def input_file(file_name):
    fin = open(file_name)
    count = 0
    all_points = []
    for line in fin:
        line = line.strip()
        if count > 0:
            line = list(map(lambda x: int(x), line.split(" ")))
            all_points.append(line)
        count += 1
    fin.close()
    return all_points


def derive_answer(input_points):
    max_length = 0
    # Use manual counting instead of using the built in index() function
    # Do this because manual counting always gives right index you are referring to. The index(function) goes to the
    # first element with the VALUE of the parameter.
    for index_value in range(len(input_points[1:-1:])):
        distance_between_all_points = find_dist([input_points[index_value], input_points[index_value+1],
                                                 input_points[index_value+2]])
        distance_between_point_removed = find_dist([input_points[index_value], input_points[index_value+2]])
        new_distance = distance_between_all_points-distance_between_point_removed
        if new_distance > max_length:
            max_length = new_distance

    return find_dist(input_points)-max_length


def output_file(input_num):
    fout = open("marathon.out", "w")
    fout.write("{}".format(input_num))
    fout.close()


output_file(derive_answer(input_file("marathon.in")))
