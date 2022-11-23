import string


def CamelCase(str):
    signs = list(string.punctuation)
    for el in str:
        if el in signs:
            str = str.replace(el, ' ')
    temp_lst = str.split()
    list_1 = [i.capitalize() for i in temp_lst]
    return ''.join(list_1)


# print(CamelCase('The-stealth!*&warrior'))
