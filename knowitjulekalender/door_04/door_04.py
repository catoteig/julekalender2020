def count_groceries(deliverylist):
    groceries2 = []
    aggregated = [0, 0, 0, 0]  # sukker, mel, melk, egg

    with open(deliverylist) as f:
        groceries = f.read().splitlines()

    for element in groceries:
        groceries2.extend(element.split(','))

    groceries2 = [x.strip() for x in groceries2]

    for element in groceries2:
        grocerytuple = element.partition(':')
        if grocerytuple[0] == 'sukker':
            aggregated[0] += int(grocerytuple[2])
        elif grocerytuple[0] == 'mel':
            aggregated[1] += int(grocerytuple[2])
        elif grocerytuple[0] == 'melk':
            aggregated[2] += int(grocerytuple[2])
        elif grocerytuple[0] == 'egg':
            aggregated[3] += int(grocerytuple[2])

    return aggregated


def calculate_cakes(deliverylist):
    aggregated_list = count_groceries(deliverylist)
    aggregated_list[0] /= 2
    aggregated_list[1] /= 3
    aggregated_list[2] /= 3

    return int(min(aggregated_list))


def test_1():
    assert calculate_cakes('leveringsliste_test.txt') == 11


print(calculate_cakes('leveringsliste.txt'))
