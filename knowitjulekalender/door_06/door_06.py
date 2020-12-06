def candy_elfs(candylist, elfs):

    with open(candylist) as f:
        candy = f.read().split(',')
        map_object = map(int, candy)
        candy = list(map_object)

    while sum(candy) % elfs != 0:
        candy.pop(len(candy) - 1)

    return int(sum(candy) / elfs)


def test_1():
    assert candy_elfs('godteri_test.txt', 9) == 13


print(candy_elfs('godteri.txt', 127))
