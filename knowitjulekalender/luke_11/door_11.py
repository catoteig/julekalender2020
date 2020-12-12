from itertools import zip_longest


def find_password(hints, answer):
    with open(hints) as f:
        pw_list = f.read().splitlines()

    for word in pw_list:
        passwords = make_passwords(word)
        for substring in passwords:
            if answer in substring:
                return word


def make_passwords(hint):
    passwords, result = [[]], []

    for letter in hint:
        passwords[0].append(letter)

    while len(hint) > 1:
        hint = hint[1:]
        new_line = ''.join(add_1_letter(letter) for letter in hint)
        temp = []
        for char_1, char_2 in zip(new_line, passwords[-1]):
            temp.append(chr(((ord(char_1) + ord(char_2) - 97 - 97) % 26) + 97))
        passwords.append(temp)
        hint = temp

    transposed = [list(filter(None, i)) for i in zip_longest(*passwords)]

    for word in transposed:
        result.append(''.join(word))

    return result


def add_1_letter(char):
    return chr(ord('a')) if char == 'z' else chr(ord(char) + 1)


def test_1():
    assert find_password('hint_test.txt', 'jeljxmw') == 'juletre'
    assert find_password('hint_test.txt', 'ugxnoj') == 'juletre'
    assert find_password('hint_test.txt', 'lqpau') == 'juletre'
    assert find_password('hint_test.txt', 'eykt') == 'juletre'
    assert find_password('hint_test.txt', 'tli') == 'juletre'
    assert find_password('hint_test.txt', 'rw') == 'juletre'
    assert find_password('hint_test.txt', 'e') == 'juletre'


print(find_password('hint.txt', 'eamqia'))
