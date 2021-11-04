def isAmicable(x):
    list = []
    sum = 0
    for i in range(1,int(x/2)+1):
        if x % i == 0:
            list.append(i)
    for j in range(0, len(list)):
        sum += int(list[j])
    return sum

result = 0

for a in range(10000):
    b = isAmicable(a)
    if isAmicable(b) == a and a != b:
        result += a
        print(a,b)

print(result)
