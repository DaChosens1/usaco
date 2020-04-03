def input_file(file_name):  # correct
    fin = open(file_name)
    count = 0
    cows_all = []
    for line in fin:
        line = line.strip()
        if count > 0:
            pos, spd = line.split(" ")
            cows_all.append(int(spd))
        count += 1
    fin.close()
    return cows_all


def cows_are_jogging(cows_spd):
    reversed_cows = [cows_spd[-1*i] for i in range(1, len(cows_spd)+1)]
    groups = [[reversed_cows[0]]]
    for cow in range(1, len(reversed_cows)):
        if reversed_cows[cow] > reversed_cows[cow-1]:
            groups[-1].append(reversed_cows[cow])
            reversed_cows[cow] = reversed_cows[cow-1]
        else:
            groups.append([reversed_cows[cow]])
    return len(groups)


def output_file(input_num):
    fout = open("cowjog.out", "w")
    fout.write("{}".format(input_num))
    fout.close()


output_file(cows_are_jogging(input_file("cowjog_bronze/3.in")))
