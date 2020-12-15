from collections import defaultdict


def parse_lists(riddle, wordlist):
    with open(riddle) as f:
        riddles = f.read().splitlines()
        riddle_list = []
        for line in riddles:
            riddle_list.append(line.split(', '))

    with open(wordlist) as f:
        words = f.read().splitlines()
        word_dict = defaultdict(int)
        for line in words:
            word_dict[line] = 0

    return riddle_list, word_dict


def find_glueword(riddles_txt, wordlist_txt):

    riddle_list, word_dict = parse_lists(riddles_txt, wordlist_txt)
    first, last, result, length = [], [], [], 0

    for riddle in riddle_list:
        for k, v in word_dict.items():
            if k.startswith(riddle[0]):
                first.append(k.replace(riddle[0], ''))
            if k.endswith(riddle[1]):
                last.append(k.replace(riddle[1], ''))

        for item in first:
            if item in last and item not in result and item in word_dict:
                result.append(item)

        first.clear()
        last.clear()

    for s in result:
        length += len(s)

    return length


def test_1():
    assert find_glueword('riddles_test.txt', 'wordlist.txt') == 14


print(find_glueword('riddles.txt', 'wordlist.txt'))
