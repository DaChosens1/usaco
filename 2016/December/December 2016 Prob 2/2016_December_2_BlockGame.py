alphabet = list("abcdefghijklmnopqrstuvwxyz")
def letters_in_pair(input_list):
    word1 = list(input_list[0])
    word2 = list(input_list[1])
    total = ""
    for let in alphabet:
        one = word1.count(let)
        two = word2.count(let)
        total += max(one, two)*let
    return total


fin = open('blocks.in')
# fin = open('ex.txt')
count = 1
blocks = []
comp_total = ""
all_letter = {}
for line in fin:
    if count != 1:
        line = line.strip()
        word1, word2 = line.split(' ')
        blocks.append([word1, word2])
    count += 1
fin.close()
for block in blocks:
    comp_total += letters_in_pair(block)
for letter in alphabet:
    ai = comp_total.count(letter)
    all_letter[letter] = ai
fout = open("blocks.out", "w")
for l in alphabet:
    fout.write("{}\n".format(all_letter[l]))
fout.close()
