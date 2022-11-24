import string


def camelCase(str):
    signs = list(string.punctuation)
    for el in str:
        if el in signs:
            str = str.replace(el, ' ')
    temp_lst = str.split()
    list_1 = [i.capitalize() if temp_lst.index(i) > 0 else i for i in temp_lst]
    return ''.join(list_1)


print(camelCase('the-stealth_warrior'))

