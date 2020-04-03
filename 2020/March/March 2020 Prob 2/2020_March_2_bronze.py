import copy
# time = 48 min


def open_file():
    fin = open('1.in')
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
    r = 99999
    for cow in cows:
        if cow[1] == 0:
            try:
                if abs(cow[0]-cows[cows.index(cow)-1][0]) < r:
                    r = abs(cow[0]-cows[cows.index(cow)-1][0])
            except:
                pass
            try:
                if abs(cow[0]-cows[cows.index(cow)+1][0]) < r:
                    r = abs(cow[0]-cows[cows.index(cow)+1][0])
            except:
                pass
    if r == 99999:
        return 1
    else:
        r -= 1
        infected_cows = copy.deepcopy(cows)
        for cow in cows:
            if cow[1] == 0:
                infected_cows.remove(cow)
        for x in range(len(infected_cows)):
            infected_cows[x] = infected_cows[x][0]
        groups = [[infected_cows[0]]]
        infected_cows.pop(0)
        for cow in infected_cows:
            works = False
            for x in range(len(groups)):
                for n in range(len(groups[x])):
                    if groups[x][n]-r <= cow <= groups[x][n]+r:
                        groups[x].append(cow)
                        works = True
                        break
                if works:
                    break
            if not works:
                groups.append([cow])
        return len(groups)


def close_file(answer):
    fout = open("socdist2.out", "w")
    fout.write("{}\n".format(answer))
    fout.close()


close_file(follow_through(open_file()))