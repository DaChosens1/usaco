def intersection(lst1):
    try :
        ai = set(lst1[0]).intersection(set(lst1[1]))

    except :
        ai = lst1[0]
    for i in range(1, len(ai)-2):
        a = ai.intersection(lst1[-1*i])
        ai = a
    return list(ai)


def input_file():
    fin = open('badmilk.in')
    # fin = open('ex.txt')
    people_drank_milk = []
    sick_people = []
    count = 0
    for line in fin:
        line = line.strip()
        if count == 0:
            line = line.split(" ")
            m = int(line[1])
            d = int(line[2])
        else:
            if count > d:
                person, time = list(map(lambda x: int(x), line.split(" ")))
                sick_people.append([person, time])
            else:
                person, time, milk = list(map(lambda x: int(x), line.split(" ")))
                people_drank_milk.append([person, time, milk])
        count += 1
    fin.close()
    return [people_drank_milk, sick_people, m]


def create_people_dict(input_list):
    all_people = {}
    for persons_milk_drank in input_list:
        if persons_milk_drank[0] in all_people.keys():
            all_people[persons_milk_drank[0]].append(persons_milk_drank[1::])
        else:
            all_people[persons_milk_drank[0]] = list()
            all_people[persons_milk_drank[0]].append(persons_milk_drank[1::])
    return all_people


def find_bad_milk(input_dict, input_list, input_len):
    possible_milk_candidates = [[] for i in range(len(input_list))]
    for sick_person in input_list:
        for milk_and_time in input_dict[sick_person[0]]:
            if milk_and_time[1] < sick_person[1]:
                possible_milk_candidates[input_list.index(sick_person)].append(milk_and_time[0])
    for possible_bad_milks in range(len(possible_milk_candidates)):
        try:
            possible_milk_candidates.remove([])
        except:
            pass
    bad_milks = intersection(possible_milk_candidates)

    return bad_milks


def derive_answer(input_dict, input_list):
    max_sick_people = 0
    for milk_candidate in input_list:
        temp = 0
        for persons_milks_and_times in list(input_dict.values()):
            for milk_drank in persons_milks_and_times:
                if milk_candidate == milk_drank[0]:
                    temp += 1
                    break
        if temp > max_sick_people:
            max_sick_people = temp
    return max_sick_people


def output_file(input_num):
    fout = open("badmilk.out", "w")
    fout.write("{}".format(input_num))
    fout.close()


total_milks, all_sick_people, amount_milks = input_file()
total_milks.sort()
all_people = create_people_dict(total_milks)
output_file(derive_answer(all_people, find_bad_milk(all_people, all_sick_people, amount_milks)))
