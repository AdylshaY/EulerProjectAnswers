import math

number = 1
i = 2
sayac = 0
while sayac * 2  < 500:
    sayac = 0
    number = number + i
    i += 1
    for j in range(2, int(math.sqrt(number))+1):
        if number % j == 0:
            sayac += 1

print(number)
