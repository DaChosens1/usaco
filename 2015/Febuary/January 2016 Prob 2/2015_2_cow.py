# time = 37 min
def open_file():
    fin = open('cow.in')
    text = []
    count = 0
    for line in fin:
        line = line.strip()
        if count != 0:
            text = [char for char in line]
        count += 1
    fin.close()
    return text


def follow_through(text):
    c = 0
    co = 0
    cow = 0
    for char in text:
        if char == "C":
            c += 1
        elif char == "O":
            co += c
        elif char == "W":
            cow += co
    return cow


def close_file(answer):
    fout = open("cow.out", "w")
    fout.write("{}".format(answer))
    fout.close()


close_file(follow_through(open_file()))