counter = 0
winnersTotal = 0
winnersName = 0
for i in range(1,1000000,2):
    n = i
    while i != 1:
        if (i % 2) == 0:
            i = i/2
        else:
            i = (3*i)+1
        counter+=1
    if counter > winnersTotal:
        winnersTotal = counter
        winnersName = n
    counter = 0
print(winnersName,": with a chain length of :",winnersTotal)