variable1 = 999
variable2 = 999
highest_palindrome = 0
while variable1 > 100:
    variable2 = 999
    while variable2 > 100:
        probable_palindrome = variable1 * variable2
        test = len(str(probable_palindrome))
        test2 = str(probable_palindrome)[test::-1]
        if str(probable_palindrome) == test2:
            if probable_palindrome > highest_palindrome:
                highest_palindrome = probable_palindrome
        variable2 -= 1
    variable1 -= 1
print(highest_palindrome)