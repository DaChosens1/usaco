def input_file(file_name):
    fin = open(file_name)
    count = 0
    all_existing_cows = []
    cows_coming_in = []
    for line in fin:
        line = line.strip()
        if count > 0:
            has_spots, lbs = line.split(" ")
            all_existing_cows.append([int(lbs), has_spots == "S"])
        else:
            cows, start, finish = line.split(" ")
            cows_coming_in = (int(start), int(finish))
        count += 1
    fin.close()
    all_existing_cows.sort()
    return all_existing_cows, cows_coming_in


def find_all_spots(all_cows):
    all_spots = 0
    existing_cows = all_cows[0]
    coming_cows = all_cows[1]
    if existing_cows[0][0] != coming_cows[0]:
        existing_cows.insert(0, [coming_cows[0], existing_cows[0][1]])
    if existing_cows[-1][0] != coming_cows[-1]:
        existing_cows.append([coming_cows[-1], existing_cows[-1][1]])
    if existing_cows[0][1]:
        all_spots += 1
    for cow in range(len(existing_cows)-1):
        if existing_cows[cow][1] == existing_cows[cow+1][1] and existing_cows[cow+1][1] is True:
            all_spots += (existing_cows[cow+1][0]-existing_cows[cow][0])
        elif not existing_cows[cow][1] and not existing_cows[cow+1][1]:
            pass
        else:
            midpoint = (existing_cows[cow][0] + existing_cows[cow+1][0])/2
            if existing_cows[cow][1]:
                midpoint//1
                all_spots += abs(midpoint - existing_cows[cow][0])
            else:
                midpoint = round(midpoint)
                all_spots += abs(midpoint - existing_cows[cow+1][0])+1
    return int(all_spots)


def output_file(input_num):
    fout = open("learning.out", "w")
    fout.write("{}".format(input_num))
    fout.close()


output_file(find_all_spots(input_file("learning_bronze/2.in")))
