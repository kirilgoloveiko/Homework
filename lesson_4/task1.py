def NOK(num1, num2):
    if num1 > num2:
        greatest = num1
    else:
        greatest = num2
    while True:
        if (greatest % num1 == 0) and (greatest % num2 == 0):
            nok = greatest
            break
        greatest += 1
    return f'NOK of "{num1}" and "{num2}" is {nok}'

