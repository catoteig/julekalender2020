def make_horizontal(matrix_txt_txt):
    horizontal_result = ''
    file = open(matrix_txt_txt, 'r')
    horizontal = file.readlines()

    for row in horizontal:
        horizontal_result += row[:-1]

    return horizontal_result + ' ' + horizontal_result[::-1]


def make_vertical(matrix_txt):
    vertical_result = ''
    file = open(matrix_txt, 'r')
    horizontal = file.readlines()

    for i in range(len(horizontal)):
        vertical_string = ''.join([word[i] for word in horizontal])
        vertical_result += vertical_string

    return vertical_result + ' ' + vertical_result[::-1]


def make_diagonal(matrix_txt):
    diagonal = ''
    file = open(matrix_txt, 'r')
    horizontal = file.readlines()

    # South -> east, X-direction
    for i in range(len(horizontal)):
        y = 0
        for x in range(len(horizontal)-i):
            diagonal += horizontal[x+i][y]
            y += 1
        diagonal += ' '

    # South -> east, Y-direction
    for i in range(len(horizontal)):
        y = 0
        for x in range(len(horizontal)-i):
            diagonal += horizontal[y][x+i]
            y += 1
        diagonal += ' '

    # South -> west, Y-direction
    for i in range(len(horizontal)):
        y = len(horizontal) - 1
        for x in range(0, len(horizontal)-i):
            diagonal += horizontal[x+i][y]
            y -= 1
        diagonal += ' '

    # South -> west, X-direction
    for i in range(len(horizontal)):
        y = 0
        for x in range(len(horizontal)-1, -1, -1):
            diagonal += horizontal[y][x-i]
            y += 1
        diagonal += ' '

    return diagonal + ' ' + diagonal[::-1]


def parse_wordlist(wordlist_txt):
    wordlist = []
    file = open(wordlist_txt, 'r')
    list = file.readlines()

    for row in list:
        wordlist.append(row[:-1])

    return wordlist
    

def find_words(matrix_txt, wordlist_txt):
    wordlist = parse_wordlist(wordlist_txt)
    horizontal = make_horizontal(matrix_txt)
    vertical = make_vertical(matrix_txt)
    diagonal = make_diagonal(matrix_txt)
    no_match = []

    for word in wordlist:
        if word not in (horizontal + vertical + diagonal):
            no_match.append(word)

    return ','.join(sorted(no_match))


def test_1():
    assert find_words('matrix_txt_test.txt', 'wordlist_test') == 'palmesøndag,påskeegg,smågodt'


print(find_words('matrix.txt', 'wordlist.txt'))
