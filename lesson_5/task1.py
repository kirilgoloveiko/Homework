some_string = 'Cause trying not to love you, only makes me love you more'  # Nickelback


def length_of_the_shortest_word(some_string: str) -> int:
    arr = some_string.split()
    min_word = min(arr, key=len)
    return len(min_word)

