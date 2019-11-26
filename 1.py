Uinput = input('Type a number: ')

intCurrent = 3
intSum = 0
while (intCurrent) <= (int(Uinput) - 1):
    intSum += intCurrent
    intCurrent +=3
intCurrent = 5
while (intCurrent) <= (int(Uinput) - 1):
    if intCurrent % 3 != 0:
        intSum += intCurrent
    intCurrent += 5
print(intSum)

