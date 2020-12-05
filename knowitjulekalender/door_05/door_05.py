def find_area(movements):
    coords, x, y, dividend = [], 0, 0, 0

    with open(movements) as f:
        moves = list(f.read())

    for i in moves:
        coords.append([x, y])
        if i == 'H': x += 1
        elif i == 'V': x -= 1
        elif i == 'O': y += 1
        elif i == 'N': y -= 1

    # Formula: A = (x1 * y2 - y1 * x2) / 2
    for i in range(len(coords) - 1):
        dividend += coords[i][0] * coords[i + 1][1] - coords[i][1] * coords[i + 1][0]

    return int(dividend / 2)


def test_1():
    assert find_area('rute_test.txt') == 14


print(find_area('rute.txt'))
