# time = 32 min
def open_file():
    fin = open('cowroute.in')
    route_cost = []
    route_dest = []
    count = 0
    for line in fin:
        line = line.strip()
        select = count%2
        if count == 0:
            start, finish, amount = map(lambda x: int(x), line.split(" "))
        elif select == 1:
            route_cost.append(map(lambda x: int(x), line.split(" "))[0])
        elif select == 0:
            route_dest.append(map(lambda x: int(x), line.split(" ")))
        count += 1
    fin.close()
    routes = []
    for n in range(len(route_cost)):
        routes.append([route_dest[n], route_cost[n]])
    return start, finish, routes


def follow_through(data):
    start, finish, routes = data
    pos_costs = []
    for route in routes:
        if start in route[0] and finish in route[0]:
            if route[0].index(start) < route[0].index(finish):
                pos_costs.append(route[1])
    return -1 if pos_costs == [] else min(pos_costs)


def close_file(answer):
    fout = open("cowroute.out", "w")
    fout.write("{}\n".format(answer))
    fout.close()


close_file(follow_through(open_file()))
