with open("problem13_input.txt") as f:
    ints = [int(line.strip()) for line in f.readlines()]

total = 0
for num in ints:
    total += num
print(total)
    