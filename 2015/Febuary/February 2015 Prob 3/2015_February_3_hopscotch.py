# time = 45 min
def open_file():
    fin = open('hopscotch_bronze/11.in')
    grid = []
    count = 1
    for line in fin:
        line = line.strip()
        if count != 1:
            grid.append([char for char in line])
        count += 1
    fin.close()
    return grid, [0, 0]


def follow_through(grid, place):
    if place == [len(grid)-1, len(grid[0])-1]:
        return 1
    elif place[0] == len(grid) or place[1] == len(grid[0]):
        return 0
    else:
        pos_next_point = []
        for a in range(place[0], len(grid)):
            for b in range(place[1], len(grid[0])):
                if grid[a][b] != grid[place[0]][place[1]]:
                    pos_next_point.append([a, b])
        vals = 0
        for n in pos_next_point:
            vals += follow_through(grid, n)
        return vals


def close_file(data):
    grid, place = data
    fout = open("hopscotch.out", "w")
    fout.write("{}".format(follow_through(grid, place)))
    fout.close()


close_file(open_file())
