import copy


def elves(elf_file):
    coordlist = make_coordlist(elf_file)
    coordlist2 = copy.deepcopy(coordlist)
    new_sick, days = True, 0
    while new_sick:
        days += 1
        new_sick = False
        for i in coordlist:
            if not coordlist[i]:  # Hvis frisk
                sick_neighbours = 0
                # nearby: [east, west, north, south]
                nearby = [(i[0] + 1, i[1]), (i[0] - 1, i[1]), (i[0], i[1] + 1), (i[0], i[1] - 1)]
                for j in nearby:
                    if j in coordlist:
                        if coordlist[j]:
                            sick_neighbours += 1
                if sick_neighbours >= 2:
                    coordlist2[i] = True
                    new_sick = True
        coordlist = copy.deepcopy(coordlist2)
    return days


def make_coordlist(coordinates):
    with open(coordinates) as f:
        parsed_coords = f.read().splitlines()

    coord_dict = {}
    for i in enumerate(parsed_coords):
        x = i[0]
        for j in enumerate(i[1]):
            y = j[0]
            coord_dict[(x, y)] = True if j[1] == 'S' else False

    return coord_dict


print(elves('elves.txt'))
