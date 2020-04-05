# time = 34 min
def open_file():
    fin = open('promote.in')
    levels = []
    for line in fin:
        line = line.strip()
        levels.append(map(lambda x: int(x), line.split(" ")))
    fin.close()
    levels.reverse()
    return levels


def follow_through(levels):
    temp = levels[::]
    answer = [0 for n in range(len(temp)-1)]
    for level in range(len(temp)-1):
        obtained = temp[level][1]-temp[level][0]
        levels[level+1] = [levels[level+1][0]-obtained, levels[level+1][1]]
        temp[level + 1] = [temp[level + 1][0] - obtained, temp[level + 1][1]]
        answer[level] = obtained
    answer.reverse()
    return answer


def close_file(answer):
    fout = open("promote.out", "w")
    for ans in answer:
        fout.write("{}\n".format(ans))
    fout.close()


close_file(follow_through(open_file()))