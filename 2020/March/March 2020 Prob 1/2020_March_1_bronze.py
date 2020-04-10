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
    def find_large_gap(stalls_list):
        temp = stalls_list
        temp = [1] + temp + [1]
        pos_location = []
        for stall in range(len(temp)):
            if temp[stall] == 1:
                for other_stall in range(stall + 1, len(temp)):
                    if temp[other_stall] == 1:
                        pos_location.append([stall, other_stall])
                        break
        max_dist = [0, 0]
        for pos_place in pos_location:
            if abs(pos_place[0] - pos_place[1]) > abs(max_dist[0] - max_dist[1]):
                max_dist = pos_place
        return [max_dist[0]-1, max_dist[1]-1]

    pos_solutions = []
    for first_cow in range(3):
        pos_sol = stalls[::]
        if first_cow == 0:
            for n in range(len(pos_sol)):
                if pos_sol[n] == 0:
                    pos_sol[n] = 1
                    break
        elif first_cow == 1:
            max_dist = find_large_gap(pos_sol)
            pos_sol[(max_dist[1]+max_dist[0])/2] = 1
        elif first_cow == 2:
            for n in range(1, len(pos_sol)+1):
                if pos_sol[-n] == 0:
                    pos_sol[-n] = 1
                    break
        temp = pos_sol[::]
        for second_cow in range(3):
            new_pos_sol = temp[::]
            if second_cow == 0:
                for n in range(len(new_pos_sol)):
                    if new_pos_sol[n] == 0:
                        new_pos_sol[n] = 1
                        break
            elif second_cow == 1:
                max_dist = find_large_gap(new_pos_sol)
                new_pos_sol[(max_dist[1] + max_dist[0]) / 2] = 1
            elif second_cow == 2:
                for n in range(1, len(new_pos_sol) + 1):
                    if new_pos_sol[-n] == 0:
                        new_pos_sol[-n] = 1
                        break
            pos_solutions.append(new_pos_sol)
    last_instance = stalls[::]
    large_gap = find_large_gap(last_instance)
    last_instance[int(large_gap[0]+round((large_gap[1]-large_gap[0])/3))] = 1
    last_instance[int(large_gap[0]+round((large_gap[1]-large_gap[0])/3*2))] = 1
    pos_solutions.append(last_instance)
    return pos_solutions


def find_d(pos_solution):
    most_min_dist = 0
    for solution in pos_solution:
        min_dist = 100005
        for filled_stall in range(len(solution)):
            for new_filled_stall in range(filled_stall+1, len(solution)):
                if filled_stall != new_filled_stall and solution[filled_stall] == 1 and solution[new_filled_stall] == 1\
                        and abs(new_filled_stall-filled_stall) < min_dist:
                    min_dist = abs(new_filled_stall-filled_stall)
        if min_dist > most_min_dist:
            most_min_dist = min_dist
    return most_min_dist


def close_file(answer):
    fout = open("socdist1.out", "w")
    fout.write("{}\n".format(answer))
    fout.close()


close_file(find_d(place_cows(open_file())))
