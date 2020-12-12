from collections import defaultdict


def find_winner(result_file):

    with open(result_file) as f:
        parsed_result = f.read().splitlines()

    result_list = []
    for i in parsed_result:
        result_list.append(i.split(','))

    score = defaultdict(int)

    for comp in result_list:
        for i, player in enumerate(comp):
            if player in score:
                score[player] += len(comp) - (i + 1)
            else:
                score[player] = len(comp) - (i + 1)

    winner_name, winner_score = '', 0
    for i in score:
        if score[i] > winner_score:
            winner_name, winner_score = i, score[i]

    return winner_name + '-' + str(winner_score)


def test_1():
    assert find_winner('leker_test.txt') == 'ae-11'


print(find_winner('leker.txt'))
