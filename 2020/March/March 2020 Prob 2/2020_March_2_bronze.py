# time = 48 min
def open_file():
    fin = open('socdist2.in')
    cows = []
    count = 1
    for line in fin:
        line = line.strip()
        if count != 1:
            cows.append(map(lambda x: int(x), line.split(" ")))
        count += 1
    fin.close()
    cows.sort()
    return cows


def follow_through(cows):
    R = 1000
    for cow in range(len(cows)):
        if cows[cow][1] == 0 and cow != len(cows) - 1 and cows[cow + 1][1] == 1:
            if cows[cow + 1][0] - cows[cow][0] < R:
                R = cows[cow + 1][0] - cows[cow][0]
        if cows[cow][1] == 0 and cow != 0 and cows[cow - 1][1] == 1:
            if cows[cow][0] - cows[cow - 1][0] < R:
                R = cows[cow][0] - cows[cow - 1][0]
    sick_cow_groups = [[]]
    for cow in cows:
        if cow[1] == 1:
            sick_cow_groups[-1].append(cow[0])
        elif cow[1] == 0 and sick_cow_groups[-1] != []:
            sick_cow_groups.append([])
    if sick_cow_groups[-1] == []:
        sick_cow_groups.pop()
    sick_cows = 0
    for group in sick_cow_groups:
        temp = group[::]
        new_groups = [[temp[0]]]
        temp.pop(0)
        for cow in temp:
            if cow - new_groups[-1][-1] >= R:
                new_groups.append([cow])
            else:
                new_groups[-1].append(cow)
        sick_cows += len(new_groups)
    return sick_cows



def close_file(answer):
    fout = open("socdist2.out", "w")
    fout.write("{}\n".format(answer))
    fout.close()


close_file(follow_through(open_file()))