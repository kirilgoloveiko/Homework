arr1 = ['a', 'b', 'b', 'c', 'b', 'c'] # -> [1, 3, 3, 2, 3, 2]


def Counter(arr1: list) -> dict:
    arr2 = []

    for item in arr1:
        arr2.append(arr1.count(item))
    print(arr2)
    final_dict = dict(zip(arr1, arr2))
    return final_dict
