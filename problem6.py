# sum of squares minus sum squared

def sumSquared(n):
    return (n*(n+1)/2) * (n*(n+1)/2)

def sumOfSquares(n):
    return n*(n+1) * (2*n+1)/6

print(sumSquared(100) - sumOfSquares(100))    