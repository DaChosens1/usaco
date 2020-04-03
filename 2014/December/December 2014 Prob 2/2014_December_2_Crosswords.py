def input_file(file_name):
    fin = open(file_name)
    count = 0
    num_rows = 0
    num_columns = 0
    all_points = []
    for line in fin:
        line = line.strip()
        if count > 0:
            line = list(line)
            all_points.append(line)
        else:
            rows, columns = line.split(" ")
            num_rows = int(rows)
            num_columns = int(columns)
        count += 1
    fin.close()
    return all_points, num_rows, num_columns


def in_area(index, length):
    return index in range(0, length)


def check_if_horizontal_lead(input_list, line, cell, num_rows):
    if not in_area(cell + 2, num_rows):
        return
    if input_list[line][cell] != "#":
        if not in_area(cell - 1, num_rows) and input_list[line][cell + 1] == "." and \
                input_list[line][cell + 2] == ".":
            input_list[line][cell] = "!"
        if input_list[line][cell - 1] == "#" and input_list[line][cell + 1] == "." and \
                input_list[line][cell + 2] == ".":
            input_list[line][cell] = "!"


def check_if_vertical_lead(input_list, line, cell, num_columns):
    if not in_area(line + 2, num_columns):
        return
    if input_list[line][cell] != "#":
        if not in_area(line - 1, num_columns) and input_list[line + 1][cell] == "." and \
                input_list[line + 2][cell] == ".":
            input_list[line][cell] = "!"
        if input_list[line - 1][cell] == "#" and input_list[line + 1][cell] == "." and \
                input_list[line + 2][cell] == ".":
            input_list[line][cell] = "!"


def if_starter(input_list, num_rows, num_columns):
    for line in range(0, num_rows):
        for cell in range(0, num_columns):
            check_if_horizontal_lead(input_list, line, cell, num_columns)
            check_if_vertical_lead(input_list, line, cell, num_rows)
    return input_list


def output_lines(input_list):
    all_lines = [0]
    for line in range(len(input_list)):
        for cell in range(len(input_list[line])):
            if input_list[line][cell] == "!":
                all_lines[0] += 1
                all_lines.append([line+1, cell+1])
    return all_lines


def output_file(input_list):
    fout = open("crosswords.out", "w")
    count = 1
    for line in input_list:
        if count == 1:
            fout.write("{}\n".format(line))
        else:
            fout.write("{} {}\n".format(line[0], line[1]))
        count += 1
    fout.close()


files = input_file("crosswords.in")
output_file(output_lines(if_starter(files[0], files[1], files[2])))
