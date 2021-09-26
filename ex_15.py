def factorial(x):
    result = 1
    while x > 0:
        result = result * x
        x -= 1
    return result

answer = factorial(40)/(factorial(20)*factorial(20))
print(int(answer))