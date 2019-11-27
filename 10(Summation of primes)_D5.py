import math
numInput = 2000000
cycle = 1
start = 1
number = 0
while cycle < numInput:
    start +=1
    sqrt_start = math.sqrt(start)
    sqrt_start = int(sqrt_start)
    for i in range(2, sqrt_start):          
        if start != i: 
            if (start % i) == 0:
                break
    else:
        number += start
    cycle+=1
print('big nibba' + str(number))