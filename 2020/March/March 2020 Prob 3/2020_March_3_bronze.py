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
    true_canidates = []
    pos_canidates = range(1, len(cows_list)+1)
    k_vals = []
    for canidate in pos_canidates:
        works = False
        for pos_k in range(len(logs)+1):
            cows_rep = [[0, 0] for n in range(len(cows_list))]
            cows_rep[canidate - 1][0] = 1
            for log in logs:
                a = False
                b = False
                if cows_rep[log[1]-1][0] == 1:
                    if cows_rep[log[1]-1][1] < pos_k:
                        a = True
                    cows_rep[log[1] - 1][1] += 1
                if cows_rep[log[2] - 1][0] == 1:
                    if cows_rep[log[2]-1][1] < pos_k:
                        b = True
                    cows_rep[log[2] - 1][1] += 1
                if a:
                    cows_rep[log[2] - 1][0] = 1
                if b:
                    cows_rep[log[1] - 1][0] = 1
            product = [x[0] for x in cows_rep]
            if product == cows_list:
                k_vals.append(pos_k)
                works = True
        if works:
            true_canidates.append(canidate)

    return len(true_canidates), min(k_vals), ("Infinity" if max(k_vals) == len(logs) else max(k_vals))


def close_file(answer):
    fout = open("tracing.out", "w")
    fout.write("{} {} {}".format(answer[0], answer[1], answer[2]))
    fout.close()


close_file(follow_through(open_file()))
