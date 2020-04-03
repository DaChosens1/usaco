# time = 43 min
def open_file():
    fin = open('pails.in')
    for line in fin:
        line = line.strip()
        milk_pails = map(lambda i: int(i), line.split(" "))
    fin.close()
    return milk_pails


def follow_through(milk_pails):
    max_fill = 0
    x, y, m = milk_pails
    for big_pail in range(0, m//y+1):
        for small_pail in range(0, (m-(y*big_pail))//x+1):
            if max_fill < y * big_pail + x * small_pail <= m:
                max_fill = y * big_pail + x * small_pail
    return max_fill


def close_file(answer):
    fout = open("pails.out", "w")
    fout.write("{}".format(answer))
    fout.close()


close_file(follow_through(open_file()))
