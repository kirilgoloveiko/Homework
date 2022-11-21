start = int(input('Enter start of range: '))
end = int(input('Enter end of range: '))
if start > end:
    start, end = end, start


def sum_range(start, end):
    summa = 0
    while start <= end:
        summa += start
        start += 1

    return summa
