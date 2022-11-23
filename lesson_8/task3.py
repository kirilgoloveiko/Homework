# 'is2 Thi1s T4est 3a' -> 'Thi1s is2 3a T4est'

def digit_in_word(word):
    return sorted(word)[0]

# print(digit_in_word('Thi1s'))


def sort_for_digit_in_words(str):
    arr = str.split()
    print(arr)
    arr.sort(key=digit_in_word)
    return ' '.join(arr)


# print(sort_for_digit_in_words('is2 Thi1s T4est 3a'))