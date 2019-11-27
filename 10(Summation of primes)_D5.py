import math
numInput = 20
cycle = 1
start = 1
number = 0
i = 2
while cycle < numInput:
    start +=1
    sqrt_start = math.sqrt(start)
    i = 2
    while i < sqrt_start + 1:
        if start != i:
            if (start % i) == 0:
                break
        i += 1
    else:
        number += start
    cycle+=1
print('big nibba' + str(number))