# find largest prime factor of 600851475143
import math
target = 600851475143
ints = [ i for i in range(2, int(math.sqrt(target))) ]
primes = []

for index, value in enumerate(ints):
    if value == -1:
        continue
    primes.append(value)
    for i in range(index, len(ints), value):
        ints[i] = -1

for i in range(len(primes)-1, 0, -1):
    if target%primes[i] == 0:
        print(primes[i])
        break
        
