x = int(input('How many digits do you want to see?: '))


def fibonacci(x):
    fib_n = [0, 1]
    while len(fib_n) < x:
        next_digit = fib_n[-1] + fib_n[-2]
        fib_n.append(next_digit)
    return fib_n
