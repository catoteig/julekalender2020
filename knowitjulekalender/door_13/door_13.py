from collections import defaultdict


def do_stuff_with_textstring(stringfile):

    with open(stringfile) as f:
        letter_string = f.read()

    count_dict, result = defaultdict(int), ''
    for letter in letter_string:
        if count_dict[letter] == ord(letter) - 97:
            result += letter

        if letter in count_dict:
            count_dict[letter] += 1
        else:
            count_dict[letter] = 1

    return result


def test_1():
    assert do_stuff_with_textstring('text_test.txt') == 'abec'


print(do_stuff_with_textstring('text.txt'))
