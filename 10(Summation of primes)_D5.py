n = 3
number = 0
while n < 2000000:
    for i in range(2,int(n**0.5) + 1):
        if (n % i) == 0:
            break
    else:
        number += n
    n+=2
print(number + 2)