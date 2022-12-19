import string
from functools import reduce

some_str = "The sunset sets at twelve o'clock" # -> '20 8 5 19 21 ..'


def letter_to_ordinal_number(some_str: str) -> str:
    new_str = some_str.lower().replace(' ', '')
    alphabet = string.ascii_lowercase

    new_str = reduce(lambda x, y: f'{x} {y}', [(alphabet.index(letter) + 1) for letter in new_str if letter in alphabet])
    return new_str
