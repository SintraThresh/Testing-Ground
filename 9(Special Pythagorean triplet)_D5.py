import math
a = 1
b = 1
c = 1
while a <= 500:
    while b <= 500:
        while c <= 500:
            total = a + b + c
            cCheck = a**2 + b**2
            if total == 1000 and (c**2 == cCheck):
                print(str(a) + " + " + str(b) + " = " + str(c) +": " + str(total))
                print(a*b*c)
                a = 1000
                b = 1000
                c = 1000
            c += 1
        c = b + 1
        b += 1
    b = a + 1
    a += 1