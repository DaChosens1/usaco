fin = open('paint.in')
#fin = open('ex.txt')
line_points = []
for line in fin:
    line = line.strip()
    one, two = line.split(" ")
    line_points.append([int(one), int(two)])
answer = 0
if line_points[0][1] < line_points[1][0] and line_points[0][0] < line_points[1][1] or \
        line_points[0][0] > line_points[1][1] and line_points[0][1] > line_points[1][0]:
    answer = line_points[0][1] - line_points[0][0] + line_points[1][1] - line_points[1][0]
else:
    temp = line_points[0] + line_points[1]
    answer = max(temp) - min(temp)
fin.close()
fout = open("paint.out", "w")
fout.write("{}".format(answer))
fout.close()
