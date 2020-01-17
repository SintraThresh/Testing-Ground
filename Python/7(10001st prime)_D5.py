numInput = 10001
cycle = 1
start = 1
while cycle <= numInput:
    start +=1
    for i in range(2, int(start**0.5 + 1)):
        if (start % i) == 0:
            break
    else:
        cycle+=1
print(start)
