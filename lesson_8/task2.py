def palindrome(num):
    for i in range(num + 1, num * 3):
        if str(i) == str(i)[::-1]:
            return i


# print(palindrome(191))

