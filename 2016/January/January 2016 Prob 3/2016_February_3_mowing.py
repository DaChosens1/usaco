# time = 45 min
def open_file():
    fin = open('mowing.in')
    cows = []
    count = 1
    for line in fin:
        line = line.strip()
        if count != 1:
            direct, move = line.split(" ")
            cows.append([direct, int(move)])
        count += 1
    fin.close()
    return cows


def follow_through(movement):
    time_mowed = [[0 for x in range(2001)] for x in range(2001)]
    cur_pos = [1000, 1000]
    time = 1
    time_mowed[cur_pos[0]][cur_pos[1]] = time
    pos_x = 100000000000
    for move in movement:
        if move[0] == "N":
            for step in range(move[1]):
                time += 1
                cur_pos[0] -= 1
                if time_mowed[cur_pos[0]][cur_pos[1]] and time - time_mowed[cur_pos[0]][cur_pos[1]] < pos_x:
                    pos_x = time - time_mowed[cur_pos[0]][cur_pos[1]]
                else:
                    time_mowed[cur_pos[0]][cur_pos[1]] = time
        elif move[0] == "S":
            for step in range(move[1]):
                time += 1
                cur_pos[0] += 1
                if time_mowed[cur_pos[0]][cur_pos[1]] and time - time_mowed[cur_pos[0]][cur_pos[1]] < pos_x:
                    pos_x = time - time_mowed[cur_pos[0]][cur_pos[1]]
                else:
                    time_mowed[cur_pos[0]][cur_pos[1]] = time
        elif move[0] == "E":
            for step in range(move[1]):
                time += 1
                cur_pos[1] += 1
                if time_mowed[cur_pos[0]][cur_pos[1]] and time - time_mowed[cur_pos[0]][cur_pos[1]] < pos_x:
                    pos_x = time - time_mowed[cur_pos[0]][cur_pos[1]]
                else:
                    time_mowed[cur_pos[0]][cur_pos[1]] = time
        elif move[0] == "W":
            for step in range(move[1]):
                time += 1
                cur_pos[1] -= 1
                if time_mowed[cur_pos[0]][cur_pos[1]] and time - time_mowed[cur_pos[0]][cur_pos[1]] < pos_x:
                    pos_x = time - time_mowed[cur_pos[0]][cur_pos[1]]
                else:
                    time_mowed[cur_pos[0]][cur_pos[1]] = time
    return -1 if pos_x == 100000000000 else pos_x


def close_file(answer):
    fout = open("mowing.out", "w")
    fout.write("{}".format(answer))
    fout.close()


close_file(follow_through(open_file()))
