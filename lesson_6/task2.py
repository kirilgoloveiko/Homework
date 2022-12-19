def minmax(string: str):
    arr = list(map(int, string.split()))
    return min(arr), max(arr)

