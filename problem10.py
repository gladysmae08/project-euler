# sum of primes
def sumOfPrimes(n):
    ints = [ i for i in range(2, n+1) ]
    total = 0
    for index, value in enumerate(ints):
        if value == -1:
            continue
        total += value
        for i in range(index, len(ints), value):
            ints[i] = -1
    return total

print(sumOfPrimes(2000000))

