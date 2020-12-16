import math


def solve_door_16(n):
    result = []
    for i in range(n):
        divisors = list(divisor_generator(i))
        sum_divisors = sum(divisors)
        if is_abundant(i, sum_divisors):
            diff = sum_divisors - 2 * i
            if is_perfect_square(diff):
                result.append(i)
    return len(result)


def is_perfect_square(n):
    return int(math.sqrt(n) + 0.5) ** 2 == n


def is_abundant(n, sum_divisors):
    return sum_divisors > 2 * n


# Generator sakset fra https://stackoverflow.com/questions/171765
def divisor_generator(n):
    large_divisors = []
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i * i != n:
                large_divisors.append(int(n / i))
    for divisor in reversed(large_divisors):
        yield divisor


print(solve_door_16(1000000))
