word = input('Enter word: ').lower()


def is_isogram(word: str):
    if len(word) == len(set(word)):
        return True
    return False
