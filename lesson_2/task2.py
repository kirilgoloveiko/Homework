digit = int(input('Enter a digit: '))


def is_even(digit):
    if digit == 0:
        return f'Enter another digit > 0'
    elif digit % 2 == 0:
        return f'digit {digit} is EVEN'
    else:
        return f'digit {digit} is ODD'

