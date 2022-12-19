#3
def mix_up(x, y):
    print(f'x = {x}, y = {y}')
    x, y = y, x
    return f'x = {x}, y = {y}'


#4
strng = input('Enter some string: ')


def str_without_first_and_last_elem(strng):
    if len(strng) > 2:
        return strng[1:-1]
    else:
        return f'!!! Enter longer string !!!'
