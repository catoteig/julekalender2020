import csv


def find_missing(number_file):

    with open(number_file) as csvfile:
        reader = csv.reader(csvfile)
        sum_items = 0
        for sequence in reader:
            for item in sequence:
                sum_items += int(item)

    sum_sequence = 100000 * (100000 + 1) / 2

    return sum_sequence - sum_items


print(find_missing('numbers.csv'))
