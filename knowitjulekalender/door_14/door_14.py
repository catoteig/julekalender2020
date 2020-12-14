import math


def create_sequence(length):

    seq_list, seq_dict = [], {}
    result = 0

    for el in range(length):

        if el < 2:
            seq_list.append(el)
            seq_dict[el] = el
        else:
            minus = seq_list[el - 2] - el
            in_dict = True if minus in seq_dict else False
            if minus > 0 and not in_dict:
                seq_list.append(minus)
                seq_dict[minus] = minus
            elif minus < 0 or in_dict:
                pluss = seq_list[el - 2] + el
                seq_list.append(pluss)
                seq_dict[pluss] = pluss

    for number in seq_list:
        if is_prime(number):
            result += 1

    return result


def is_prime(number):
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    for i in range(5, int(math.sqrt(number)) + 1, 6):
        if number % i == 0 or number % (i + 2) == 0:
            return False
    return True


print(create_sequence(1800813))
