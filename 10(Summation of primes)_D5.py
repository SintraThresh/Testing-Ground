n = 2000000
total = 0
primeArray = [True] * n
for i in range(2,n):
    if primeArray[i]:
        currentNum = i
        total += i
        currentNum = currentNum**2
        while currentNum < n:
            primeArray[currentNum] = False
            currentNum += i
print(str(total))