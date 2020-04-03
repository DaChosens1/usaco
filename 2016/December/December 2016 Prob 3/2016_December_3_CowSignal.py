fin = open('cowsignal.in')
# fin = open('ex.txt')
count = 1
message = []
lw = []
multiply = 0
all_letter = {}
for line in fin:
    line = line.strip()
    if count == 1:
        length, width, multiplier = list(map(lambda x: int(x), line.split(' ')))
        lw = [length, width]
        multiply = multiplier
    else:
        message.append(list(line))
    count += 1
for lines in range(lw[0]):
    for chars in range(lw[1]):
        message[lines][chars] *= multiply
for lines in range(lw[0]):
    message[lines] = "".join(message[lines])
fin.close()
fout = open("cowsignal.out", "w")
for line in message:
    for i in range(multiply):
        fout.write("{}\n".format(line))
fout.close()
