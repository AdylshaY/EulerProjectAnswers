list = []
for i in range(100,1000):
    for j in range(100,1000):
        result = i * j
        x = str(result)
        if x[0] == x[-1] and x[1] == x[-2] and x[2] == x[-3]:
            list.append(result)
            
print(max(list))
