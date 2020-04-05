# time = 34 min
def open_file():
    fin = open('angry.in')
    bales = []
    count = 0
    for line in fin:
        line = line.strip()
        if count > 0:
            bales.append(int(line))
        count += 1
    fin.close()
    bales.sort()
    return bales


def follow_through(bales):
    max_boom = 1
    for bale in range(len(bales)):
        time = 0
        all_exploded = [bales[bale]]
        left_explode = bale
        right_explode = bale
        while True:
            time += 1
            exploded = []
            for n in range(1, time+1):
                if (bales[right_explode] + n) in bales and (bales[right_explode] + n) not in all_exploded:
                    all_exploded.append(bales[right_explode] + n)
                    exploded.append(bales[right_explode] + n)
                if (bales[left_explode] - n) in bales and (bales[left_explode] - n) not in all_exploded:
                    all_exploded.append(bales[left_explode] - n)
                    exploded.append(bales[left_explode] - n)
            if exploded == []:
                break
            left_explode = bales.index(min(exploded))
            right_explode = bales.index(max(exploded))
        if len(all_exploded) > max_boom:
            max_boom = len(all_exploded)
    return max_boom


def close_file(answer):
    fout = open("angry.out", "w")
    fout.write("{}".format(answer))
    fout.close()


close_file(follow_through(open_file()))
