import math

number = 2000000
result = 2
list = [2]

for i in range(3, number):
    for j in range(2, int(math.sqrt(i))+1):
        if i % j == 0:
            break
    else:
        list.append(i)
        result += i
        
print(result)
