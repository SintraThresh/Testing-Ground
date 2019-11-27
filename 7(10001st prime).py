uInput = input('Enter number: ')
numInput = int(uInput)
cycle = 1
start = 2
counter = 0
while cycle <= numInput:
        
    for i in range(2, start):          
        if start != i: 
            if (start % i) == 0:
                counter = 1
                break
    else:
        print(start) 
    