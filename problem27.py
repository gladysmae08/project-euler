from math import sqrt

def genPrimes(n):
    '''generate primes up to n'''
    numbers = [x for x in range(1, n+1)]
    marked = [True] * n
    # Use siv to eliminate non-primes
    for x in range(2, int(sqrt(n)+1)):
        if not marked[x-1]: continue
        factor = 2
        while x*factor-1 < n:
            marked[x*factor-1] = False
            factor += 1
    # Create prime list
    primes = []
    for i,v in enumerate(marked):
        if v: primes.append(numbers[i])
    return primes

def testQuadratic(a,b,siv):
    '''Returns the number of consecutive primes generated by the quadratic 
    formula defines as n^2 + an + b
    '''
    count = 0
    while True:
        n = count
        result = n*n + a*n + b
        if result > siv[-1]:
            raise ValueError
        if binarySearch(result, siv):
            count += 1
        else:
            return count

def binarySearch(value, siv):
    '''check for value in siv using binary search'''
    import bisect
    i = bisect.bisect_left(siv, value)
    if i != len(siv) and siv[i] == value:
        return True
    return False

if __name__ == '__main__':
    import timeit
    start_time = timeit.default_timer()
    siv = genPrimes(20000)
    elapsed = timeit.default_timer() - start_time
    print("gen time: %s" % elapsed)
    # loop through possible values for a and b coefficients
    siv2 = [ x for x in siv if x < 1000 ]
    siv2 += [ -x for x in siv2 ]
    max = 0
    best_a = 0
    best_b = 0
    start_time = timeit.default_timer()
    for a in siv2:
        for b in siv2:
            count = testQuadratic(a, b, siv)
            if count > max:
                max = count
                best_a = a
                best_b = b
    elapsed = timeit.default_timer() - start_time
    print("a: %s; b: %s; count: %s; product: %s" % (best_a, best_b, max, best_a * best_b))
    print("quad time: %s" % elapsed)
