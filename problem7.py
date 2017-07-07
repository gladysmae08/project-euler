# find the nth prime
# n*log(n) + nlog(log(n))
import math
from timeit import default_timer

def upperBound(n):
    return int(math.ceil(n*math.log(n) + n*math.log(math.log(n))))

def nthPrime(n):
    ints = [i for i in range(2, upperBound(n))]
    prime_count = 0
    latest_prime = 0    
    for index, value in enumerate(ints):
        if value == -1:
            continue
        prime_count += 1
        latest_prime = value
        if prime_count == n:
            return latest_prime
        for i in range(index, len(ints), value):
            ints[i] = -1

if __name__ == "__main__":    
    start = default_timer() 
    print(nthPrime(10001))
    total_time = default_timer() - start
    print("time: ", total_time)
    
        
