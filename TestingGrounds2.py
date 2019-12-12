values = [1,2,3,4,5,6,7,8,9]
testy = [(r,c) for r in range(3) for c in range(3)]

n = 0
for testy, value in zip(testy, values):
    n += 1
    print(str(n))
print(testy)