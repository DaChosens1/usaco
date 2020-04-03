fin = open('square.in')
#fin = open('ex.txt')
count = 1
for line in fin:
    if count == 1:
        line = line.strip()
        x1, y1, x2, y2 = list(map(lambda x: int(x), line.split(' ')))
    if count == 2:
        line = line.strip()
        x3, y3, x4, y4 = list(map(lambda x: int(x), line.split(' ')))
    count += 1
fin.close()
leftmostx = min(x1, x3)
rightmostx = max(x2, x4)
bottommosty = min(y1, y3)
topmosty = max(y2, y4)
side = max(topmosty-bottommosty, rightmostx-leftmostx)
fout = open("square.out", "w")
fout.write("{}".format(side ** 2))
fout.close()
