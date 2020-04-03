fin = open('speeding.in')
# fin = open('ex.txt')
line_points = []
m = []
n = []
current_len_n = 0
current_len_m = 0
count = 0
for line in fin:
    line = line.strip()
    if count == 0:
        iteration = int(line.split(" ")[0])
    else:
        if count > iteration:
            length, spd = list(map(lambda x: int(x), line.split(" ")))
            current_len_n += length
            n.append([current_len_n, spd])
        else:
            length, spdlimit = list(map(lambda x: int(x), line.split(" ")))
            current_len_m += length
            m.append([current_len_m, spdlimit])
    count += 1
max_spd_over = 0
for dist in range(100):
    for lists in m:
        if lists[0] >= dist+1:
            spd_limit = lists[1]
            break
    for lists in n:
        if lists[0] >= dist+1:
            spd = lists[1]
            break
    if spd-spd_limit > max_spd_over:
        max_spd_over = spd-spd_limit
fin.close()
fout = open("speeding.out", "w")
fout.write("{}".format(max_spd_over))
fout.close()
