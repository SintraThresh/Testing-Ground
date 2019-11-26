n = 2
halting_factor = 71

while n <= 600851475143:
    if 600851475143 % n == 0:
        test = 0
        while test < n:
            if n == 71:
                pass
            elif n % halting_factor == 0:
                print("^That is the Highest prime factor of:^")
                n = 600851475143
                break
            test += 1
        print(n)
    n += 1