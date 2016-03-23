import math
def permutations(n):
    return math.factorial(2*n) / math.factorial(n) / math.factorial(n)
print(permutations(20))


