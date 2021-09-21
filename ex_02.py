list = [1,2]
i = 0
sum = 0
while sum < 4000000:
    x = list[-1] + list[-2]
    list.append(x)
    if list[i] % 2 == 0:
        # print(list[j])
        sum += list[i]
    i += 1
# print(list)
    
print(sum)
