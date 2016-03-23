# fibonacci sum even numbers less than 4 million
first = 1
second = 2
total = 2
while (first + second) < 4000000:
    temp = first
    first = second
    second = temp + second
    if second%2 == 0:
        total += second
print(total)
    