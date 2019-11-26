Sum = 0
counter = 0
while counter < 1000:
    if counter % 3 == 0:
        Sum = Sum + counter
    elif counter % 5 == 0:
        Sum = Sum + counter
    counter += 1
print (Sum)