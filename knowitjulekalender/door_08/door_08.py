from ast import literal_eval as make_tuple


def parse_coordinates(travel_log):
    destinations, travels = {}, []

    with open(travel_log) as f:
        raw_list = f.read().splitlines()
    for i in raw_list:
        if i[-1] == ')':
            destinations[i.partition(':')[0]] = [make_tuple(i.rpartition(': ')[2]), 0]
        else:
            travels.append(i.partition(':')[0])

    return destinations, travels


def find_delay(distance):
    if distance == 0:
        return 0
    elif distance < 5:
        return 0.25
    elif distance < 20:
        return 0.5
    elif distance < 50:
        return 0.75
    else:
        return 1


def travel(travel_log):
    destinations, travels = parse_coordinates(travel_log)
    curr_city = (0, 0)

    for stop in travels:
        next_city = destinations[stop][0]
        move_x = next_city[0] - curr_city[0]
        move_y = next_city[1] - curr_city[1]

        # X-direction:
        for point in range(1, abs(move_x) + 1):
            pos = (curr_city[0] + point, curr_city[1]) if move_x > 0 else (curr_city[0] - point, curr_city[1])
            for city in destinations:
                this_city = destinations[city][0]
                distance = abs(this_city[0] - pos[0]) + abs(this_city[1] - pos[1])
                destinations[city][1] += find_delay(distance)

        # Y-direction:
        for point in range(1, abs(move_y) + 1):
            pos = (next_city[0], curr_city[1] + point) if move_y > 0 else (next_city[0], curr_city[1] - point)
            for city in destinations:
                this_city = destinations[city][0]
                distance = abs(this_city[0] - pos[0]) + abs(this_city[1] - pos[1])
                destinations[city][1] += find_delay(distance)

        curr_city = next_city

    list_of_delays = []
    for i in destinations:
        list_of_delays.append(destinations[i][1])

    return max(list_of_delays) - min(list_of_delays)


def test_1():
    assert travel('input_test.txt') == 0.25


print(travel('input_test.txt'))
