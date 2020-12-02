import math


def packages_delivered(package_count):

    delivered, skip = 0, 0

    for i in range(0, package_count):
        if skip == 0:
            if str(i).find('7') != -1:
                for j in range(i, 0, -1):
                    if isprime(j):
                        skip = j
                        break
            else:
                delivered += 1
        elif skip > 0:
            skip -= 1

    return delivered


def isprime(number):
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


def test_1():
    assert packages_delivered(10) == 7


def test_2():
    assert packages_delivered(20) == 9


def test_3():
    assert packages_delivered(10000) == 32


print(packages_delivered(5433000))
