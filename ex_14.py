def step_counter(num):
    step = 0
    while num > 1:
        if num % 2 == 0:
            num = (num/2)
            step += 1
        else:
            num = (3*num) + 1
            step += 1
    return step

def longest_collatzs_sequence():
    longest_step = 0
    number = 0
    for i in range(0,1000000):
        step_counter(i)
        if step_counter(i) > longest_step:
            longest_step = step_counter(i)
            number = i
    return longest_step, number

print(longest_collatzs_sequence())
