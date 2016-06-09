'''fibonacci sequence'''

def add_lists(L1, L2):
    if len(L1) >= len(L2):
        large_num = L1[::-1]
        small_num = L2[::-1]
    else:
        large_num = L2[::-1]
        small_num = L1[::-1]        
        
    carry_over = 0
    for index, value in enumerate(large_num):
        if len(small_num) > index:
            sum = small_num[index] + value + carry_over
        else:
            sum = value + carry_over
        large_num[index] = sum % 10
        carry_over = int(sum / 10)
        
    if carry_over == 1:
        large_num.append(1)
    return large_num[::-1]

def fibonacci():
    current = [1]
    next = [1]
    count = 2
    while len(next) < 1000:
        temp = next[:]
        next = add_lists(current, next)
        current = temp
        count += 1
    return count

print(fibonacci())