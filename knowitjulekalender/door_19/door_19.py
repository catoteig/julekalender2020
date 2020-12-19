from collections import defaultdict
import operator


def parse_list(list_txt):

    with open(list_txt) as f:
        elf_list = []
        f_text = f.read().splitlines()
        for line in f_text:
            t = []
            t.extend(line.split(' ', 2))
            s = t[2][1:-1]
            t[0], t[1], t[2] = int(t[0]), int(t[1]), s.split(', ')
            elf_list.append(t)

    return elf_list


def find_winner(list_txt):
    game_list = parse_list(list_txt)
    winner_list = defaultdict(int)
    for game in game_list:
        winner = ''
        if game[0] == 1:
            winner = rule_1(game[1], game[2])
        elif game[0] == 2:
            winner = rule_2(game[1], game[2])
        elif game[0] == 3:
            winner = rule_3(game[1], game[2])
        elif game[0] == 4:
            winner = rule_4(game[1], game[2])

        if winner in winner_list:
            winner_list[winner] += 1
        else:
            winner_list[winner] = 1

    return max(winner_list.items(), key=operator.itemgetter(1))[0]


def rule_1(steps, order):
    while len(order) > 1:
        for i in range(steps):
            order.insert(0, order[-1])
            order.pop(-1)
        order.pop(0)

    return order[0]


def rule_2(steps, order):
    pop_chair = 0
    while len(order) > 1:
        for i in range(steps):
            order.insert(0, order[-1])
            order.pop(-1)
        order.pop(pop_chair)
        if pop_chair < len(order) - 1:
            pop_chair += 1
        else:
            pop_chair = 0

    return order[0]


def rule_3(steps, order):
    while len(order) > 1:
        for i in range(steps):
            order.insert(0, order[-1])
            order.pop(-1)
        if len(order) <= 2:
            order.pop(0)
        elif len(order) % 2 == 0:
            p = int(len(order) / 2)
            order.pop(p)
            order.pop(p - 1)
        else:
            order.pop(int(len(order)/2))

    return order[0]


def rule_4(steps, order):
    while len(order) > 1:
        for i in range(steps):
            order.insert(0, order[-1])
            order.pop(-1)
        order.pop(-1)

    return order[0]


print(find_winner('input.txt'))
