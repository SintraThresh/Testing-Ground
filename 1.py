UserInput = input('chose a number:')

Sum = 0
counter = 0
while counter < int(UserInput):
    if counter % 3 == 0:
        Sum = Sum + counter
    elif counter % 5 == 0:
        Sum = Sum + counter
    counter += 1
print (Sum)