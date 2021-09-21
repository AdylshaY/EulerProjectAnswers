import math

list = []
list2 = []
number = 600851475143
for i in range(2, int(math.sqrt(number)) + 1
    if number % i == 0:
        list.append(i)
print(f"Tam bölenler: {list}")

j = 0
while j < len(list):
    for k in range(2, list[j]):
        if list[j] % k == 0:
            break
    else:
        list2.append(list[j])
    j += 1

print(f"Tam bölenlerden asal olanlar: {list2}")
