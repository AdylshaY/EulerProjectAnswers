def factorial(x):
    result = 1
    while x > 0:
        result *= x
        x -= 1
    return result

result = str(factorial(100))
sum = 0

for i in range(0, len(result)):
    sum = int(result[i]) + sum

print(sum)