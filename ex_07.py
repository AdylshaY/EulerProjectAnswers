list = []
i = 2
while len(list) < 10001:
    for j in range(2, int(i ** 0.5)+1):
        if i % j == 0:
            i += 1
            break
    else:
        list.append(i)
        i += 1

print(list[-1])
