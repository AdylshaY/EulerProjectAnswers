result = 0
result2 = 0

for i in range(1,101):
    result += i * i
    result2 += i
    
print((result2 ** 2) - result )
