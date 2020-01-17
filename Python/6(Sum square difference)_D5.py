uInput = 100

n = 1
numSum = 0
while n <= int(uInput):
    number = n
    number *=number
    numSum += number
    n +=1
n = 1
number2 = 0
while n <= int(uInput):
    number2 += n
    n += 1
number2 *=number2
solution = (number2 - numSum)
print(str(solution))

