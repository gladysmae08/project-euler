def getAllPrimes(n):
    primes = []
    ints = [i for i in range(2, n)]
    for index, value in enumerate(ints):
        if value == -1:
            continue
        primes.append(value)
        for i in range(index, len(ints), value):
            ints[i] = -1
    return primes
        
    
def getDivisorCount(num, primes):
    finalCount = 1
    for prime in primes:
        if (num%prime != 0):
            continue
        count = 0
        while(num%prime == 0):
            count += 1
            num = num / prime
        finalCount = finalCount * (count + 1)
        if (num == 1):
            break
    return finalCount

index = 1
triangle = 0
primes = getAllPrimes(100000)
print("done with primes")
while(True):
    triangle += index
    count = getDivisorCount(triangle, primes)
    print(triangle, count)
    if (count > 500):
        print(triangle)
        break
    index += 1