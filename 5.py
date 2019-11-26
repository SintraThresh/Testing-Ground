check = 0
n = 20
while check != 1:
    test = 20
    while  test > 0 and n % test == 0:
        if test == 1:
            print(n)
            check = 1
        test -= 1
    n += 20