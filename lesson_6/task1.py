def is_simple(digit: int) -> bool:
    counter = 0
    for num in range(2, (digit//2) + 1):
        if digit % num == 0:
            counter += 1
    if counter == 0:
        return True
    return False
