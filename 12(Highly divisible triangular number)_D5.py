startingNum = 0
increm = 1
cycle = 0
highest_divisor = 0
while cycle != 1:
    divisors = 1
    finalNum = startingNum + increm
    increm +=1
    for x in range(2,int(finalNum**0.5) + 1):
        if finalNum % x == 0 and finalNum % 2 == 0 and finalNum % 5 == 0 and finalNum % 10 == 0:
            for i in range(1,finalNum):
                if finalNum % i == 0:
                    divisors +=1
            else:
                break
    if divisors > highest_divisor:
        highest_divisor = divisors
        print(str(finalNum) + ':' + str(divisors)) 
    if divisors > 500:
        cycle +=1
    startingNum = finalNum
print(str(finalNum) + ':' + str(divisors))