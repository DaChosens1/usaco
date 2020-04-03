# time = 48 min
def open_file():
    fin = open('tracing.in')
    logs = []
    count = 1
    for line in fin:
        line = line.strip()
        if count == 2:
            sick_cows = [int(char) for char in line]
        if count > 2:
            logs.append(map(lambda x: int(x), line.split(" ")))
        count += 1
    fin.close()
    logs.sort()
    return sick_cows, logs


def follow_through(data):
    cows_list, logs = data
    pos_canidates = []
    for cow in range(len(cows_list)):
        if cows_list[cow] == 1:
            pos_canidates.append(cow)
    sick_cows = pos_canidates[::]
    original_canidates = pos_canidates[::]
    pos_k = []
    for canidate in pos_canidates:
        cow_k = 10000
        pos_sick = []
        works = True
        for log in logs:
            if log[1]-1 == canidate:
                connect = log[2] - 1
                pos_sick.append(connect)
            elif log[2]-1 == canidate:
                connect = log[1] - 1
                pos_sick.append(connect)
        for sick in range(len(pos_sick)):
            try:
                sick_cows.remove(pos_sick[sick])
                if sick + 1 < cow_k:
                    cow_k = sick + 1
            except:
                if sick_cows != []:
                    works = False
                else:
                    if sick + 1 < cow_k:
                        cow_k = sick + 1
        if not works:
            original_canidates.remove(canidate)
        if canidate in original_canidates:
            pos_k.append(cow_k)
    return len(pos_canidates), min(pos_k), max(pos_k)


def close_file(answer):
    fout = open("tracing.out", "w")
    fout.write("{} {} {}".format(answer[0], answer[1], "Infinity" if answer[2] == answer[1] else answer[2]))
    fout.close()


close_file(follow_through(open_file()))
