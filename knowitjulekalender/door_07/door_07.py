from operator import xor

# Did modify the txt-files before running code


def count_usable_trees(forestfile):
    with open(forestfile) as f:
        forest = f.read().splitlines()
        forest.reverse()

    height = len(forest)
    sym_trees = 0

    for x in range(len(forest[0])):
        if forest[0][x] == '#':
            if is_symmetric(forest, height, x):
                sym_trees += 1

    return sym_trees


def is_symmetric(forest, height, x):
    for y in range(height):
        if forest[y][x] == '#':
            ut = 0
            while True:
                if xor(forest[y][x - ut] == '#', forest[y][x + ut] == '#'):
                    return False
                elif forest[y][x - ut - 1] == ' ' and forest[y][x + ut + 1] == ' ':
                    break
                else:
                    ut += 1
        elif forest[y][x - 1] == '#' or forest[y][x + 1] == '#':
            return False
        else:
            return True


def test_1():
    assert count_usable_trees('forest_test.txt') == 2


print(count_usable_trees('forest.txt'))
