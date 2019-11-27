numInput = 2000000
cycle = 1
start = 1
number = 0
while cycle < numInput:
    start +=1
    for i in range(2, start//2):          
        if start != i: 
            if (start % i) == 0:
                break
    else:
        number += start
        print(start)
    cycle+=1
print('big nibba' + str(number))