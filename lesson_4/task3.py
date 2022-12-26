import random


def filling_of_list(lenth):
    arr = []
    for _ in range(lenth):
        arr.append(random.randint(1, 10))
    return arr


def count_of_repeating_numbers(list):
    some_dict = {}
    for item in list:
        if list.count(item) > 1:
            some_dict[item] = list.count(item)
    return f'count_of_repeating_numbers is {len(some_dict)}'

