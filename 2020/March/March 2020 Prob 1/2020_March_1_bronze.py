# time = 48 min
def open_file():
    fin = open('socdist1.in')
    count = 1
    for line in fin:
        line = line.strip()
        if count != 1:
            stalls = map(lambda x: int(x), [char for char in line])
        count += 1
    fin.close()
    return stalls


def place_cows(stalls):
    new_stalls = stalls[::]
    pos_location = []
    for stall in range(len(stalls)):
        if stalls[stall] == 1:
            for other_stall in range(stall + 1, len(stalls)):
                if stalls[other_stall] == 1:
                    pos_location.append([stall, other_stall])
                    break
    max_dist = [0, 0]
    for pos_place in pos_location:
        if abs(pos_place[0] - pos_place[1]) > abs(max_dist[0] - max_dist[1]):
            max_dist = pos_place
    if pos_location[0][0] + 1 > abs(max_dist[0] - max_dist[1]):
        new_stalls[0] = 1
    elif len(pos_location) - pos_location[-1][-1] - 2 > abs(max_dist[0] - max_dist[1]):
        new_stalls[-1] = 1
    else:
        new_stalls[(max_dist[0] + max_dist[1]) // 2] = 1
    return new_stalls


def find_d(stalls):
    other_dist = 999999
    other_stalls = stalls[::]
    pos_location = []
    for stall in range(len(stalls)):
        if stalls[stall] == 1:
            for other_stall in range(stall + 1, len(stalls)):
                if stalls[other_stall] == 1:
                    pos_location.append([stall, other_stall])
                    break
    max_dist = [0, 0]
    for pos_place in pos_location:
        if abs(pos_place[0] - pos_place[1]) > abs(max_dist[0] - max_dist[1]):
            max_dist = pos_place
    if pos_location[0][0] + 1 > abs(max_dist[0] - max_dist[1]):
        other_stalls[0] = 1
        other_stalls[(pos_location[0][0] + 1)//2] = 1
    elif len(pos_location) - pos_location[-1][-1] - 2 > abs(max_dist[0] - max_dist[1]):
        other_stalls[-1] = 1
        other_stalls[len(pos_location) - pos_location[-1][-1] - 2 // 2] = 1
    else:
        other_stalls[(max_dist[0] + max_dist[1]) // 3] = 1
        other_stalls[(max_dist[0] + max_dist[1]) * 2 // 3] = 1
    new_one_locations = []
    for stall in range(len(other_stalls)):
        if other_stalls[stall] == 1:
            new_one_locations.append(stall)
    dists = []
    for x in range(len(new_one_locations) - 1):
        dists.append(abs(new_one_locations[x] - new_one_locations[x + 1]))
    pos_ans = min(dists)

    stalls = place_cows(stalls)
    stalls = place_cows(stalls)
    one_locations = []
    for stall in range(len(stalls)):
        if stalls[stall] == 1:
            one_locations.append(stall)
    dists = []
    for x in range(len(one_locations) - 1):
        dists.append(abs(one_locations[x] - one_locations[x + 1]))
    return min(dists) if min(dists) > pos_ans else pos_ans


def close_file(answer):
    fout = open("socdist1.out", "w")
    fout.write("{}\n".format(answer))
    fout.close()


close_file(find_d(open_file()))
