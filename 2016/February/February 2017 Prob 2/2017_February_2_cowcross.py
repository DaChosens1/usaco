# time = 24 min
def open_file():
    fin = open('cbarn.in')
    count = 0
    cows = []
    for line in fin:
        line = line.strip()
        if count > 0:
            cows.append(int(line))
        count += 1
    fin.close()
    return cows


def follow_through(cows):
    min_dist = 1000000000000
    temp = cows[::]
    for n in range(len(cows)):
        dist = 0
        hold = temp[0]
        temp = temp[1::]
        temp.append(hold)
        for i in range(len(temp)):
            dist += i * temp[i]
        if dist < min_dist:
            min_dist = dist
    return min_dist


def close_file(answer):
    fout = open("cbarn.out", "w")
    fout.write("{}".format(answer))
    fout.close()


close_file(follow_through(open_file()))
