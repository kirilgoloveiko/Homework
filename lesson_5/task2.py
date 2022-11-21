xo = input('enter xo-string: ')
xo = xo.lower()


def check(xo: str) -> bool:
    if xo.count('x') == xo.count('o'):
        return True
    return False
