import math
from timeit import default_timer

def primeSiv(n):
    '''return list of primes up to n'''
    numbers = [True] * (n + 1)
    numbers[0] = False # 0 is not prime
    numbers[1] = False # 1 is not prime
    for i in range(2, int(math.sqrt(n)) + 1):
        if numbers[i] == False:
            continue
        multiple = 2
        product = i * multiple
        while(product < n + 1):
            numbers[product] = False
            multiple += 1
            product = multiple * i
    return numbers

def getCircularPrimes(n):
    numbers = primeSiv(n)
    circular_primes = []
    for idx, prime in enumerate(numbers):
        if prime:
            prime_str = str(idx)
            circular = True
            for i in range(len(prime_str) - 1):
                prime_str = prime_str[1:] + prime_str[0]
                if numbers[int(prime_str)] == False:
                    circular = False
                    break
            if circular:
                circular_primes.append(idx)
    return circular_primes

if __name__ == "__main__":
    start = default_timer()
    circularPrimes = getCircularPrimes(1000000)
    print(circularPrimes)
    print(len(circularPrimes))
    total_time = default_timer() - start
    print("time: ", total_time)