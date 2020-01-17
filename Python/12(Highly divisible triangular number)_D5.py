import math
cycle = 0
currentNum = 1
currentCycle = 1
divisors = 0
while cycle == 0:
    for x in range(1, int(math.ceil(math.sqrt(currentNum)))):
        if currentNum % x == 0:
            divisors +=2
    print(f'Current number: {currentNum} Number of Divisors: {divisors}')
    if divisors > 500:
        cycle +=1
    else:
        currentCycle +=1
        currentNum = currentNum + currentCycle
        divisors = 0
