# Problem 33
# Curious fractions, 49/98 == 4/8

from timeit import default_timer

def reduce(x, y):
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    while True:
        reduced = False
        for p in primes:
            if x % p == 0 and y % p == 0:
                x = x / p
                y = y / p
                reduced = True
        if not reduced:
            break
    return x, y

def isCurious(numerator, denominator):
    n1 = int(numerator / 10)
    n2 = numerator % 10
    d1 = int(denominator / 10)
    d2 = denominator % 10
    if n1 == d1:
        return (numerator / denominator == n2 / d2)
    elif n1 == d2:
        return (numerator / denominator == n2 / d1)
    elif n2 == d1:
        return (numerator / denominator == n1 / d2)
    elif n2 == d2:
        return (numerator / denominator == n1 / d1)
    else:
        return False

if __name__ == "__main__":
    start = default_timer()
    n_prod = 1
    d_prod = 1
    for numerator in range(10, 99):
        for denominator in range(numerator + 1, 100):
            if numerator % 10 == 0 or denominator % 10 == 0:
                continue
            if isCurious(numerator, denominator):
                print("%s/%s" % (numerator, denominator))
                n_prod *= numerator
                d_prod *= denominator
    print("before: %s/%s" % (n_prod, d_prod))
    x, y = reduce(n_prod, d_prod)
    total_time = default_timer() - start
    print("after: %s/%s" % (x, y))
    print(total_time)





