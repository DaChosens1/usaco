# time = 37 min
def open_file():
    fin = open('censor.in')
    text = []
    censor = []
    count = 0
    for line in fin:
        line = line.strip()
        if count == 0:
            text = [char for char in line]
        elif count == 1:
            censor = [char for char in line]
        count += 1
    fin.close()
    return text, censor


def follow_through(data):
    text, censor = data[::]
    new_text = []
    for char in text:
        new_text.append(char)
        temp = new_text[-1:-len(censor)-1:-1]
        temp.reverse()
        if temp == censor:
            for n in range(len(censor)):
                new_text.pop()
    ans = ""
    for char in new_text:
        ans += char
    return ans


def close_file(answer):
    fout = open("censor.out", "w")
    fout.write("{}".format(answer))
    fout.close()


close_file(follow_through(open_file()))
