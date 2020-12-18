from collections import defaultdict


def parse_map(map_txt):
    map_dict = defaultdict(str)

    with open(map_txt) as f:
        words = f.read().splitlines()
        y_len = len(max(words, key=len))
        x_len = len(words)
        for line in enumerate(words):
            for coord in enumerate(line[1]):
                map_dict[(line[0], coord[0])] = coord[1]

    return map_dict, x_len, y_len


def vacuum(map_txt):
    map_dict, x_len, y_len = parse_map(map_txt)

    for x in range(x_len):
        for y in range(y_len):
            if map_dict[(x, y)] != 'x':
                spacelist = space(map_dict, x, y)
                if spacelist:
                    for i in spacelist:
                        if i in map_dict:
                            if map_dict[i] == ' ':
                                map_dict[i] = '.'

    return sum(map(' '.__eq__, map_dict.values()))


def space(map_dict, x, y):
    vacuum_space = []

    for x1 in range(x-3, x+4):
        for y1 in range(y-3, y+4):
            if (x1, y1) not in map_dict:
                return []
            elif (((x1 - x) ** 2) + ((y1 - y) ** 2)) <= 10:  # check if inside circle
                if map_dict[(x1, y1)] == 'x':
                    return []
            vacuum_space.append((x1, y1))

    vacuum_space += (x-4, y-4), (x-4, y-3), (x-4, y-2), (x-4, y+2), (x-4, y+3), (x-4, y+4), (x-3, y-4), (x-3, y+4), (x-2, y-4), (x-2, y+4)
    vacuum_space += (x+3, y-4), (x+3, y+4), (x+2, y-4), (x+2, y+4), (x+4, y-4), (x+4, y-3), (x+4, y-2), (x+4, y+2), (x+4, y+3), (x+4, y+4)

    return vacuum_space


print(vacuum('kart.txt'))
