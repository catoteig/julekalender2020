from collections import defaultdict


def find_generations(family_tree):

    with open(family_tree) as f:
        descendants = f.read()
        desc_list = descendants.split(' ')

    tree = defaultdict(list)
    gen = 0

    for elf in desc_list:

        leading, trailing = elf.count('('), elf.count(')')

        if leading > 0:
            gen += leading

        if gen in tree:
            tree[gen].append(elf)
        else:
            tree[gen] = [elf]

        if trailing > 0:
            gen -= trailing

    largest_gen = 0
    for i in tree:
        if len(tree[i]) > largest_gen:
            largest_gen = len(tree[i])

    return largest_gen


def test_1():
    assert find_generations('family_test.txt') == 6


print(find_generations('family.txt'))