# sum of factors of a is equal to b; and sum of factors of b is equal to and
'''
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
'''
from math import sqrt

def sumOfFactors(num):
    sum = 1
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            sum += i
            if num / i != i:
                sum += num / i
    return int(sum)

dList = [0,0]
for i in range(2, 10001):
    dFunc = sumOfFactors(i)
    dList.append(dFunc)

sum = 0
for index,value in enumerate(dList):
    if value != 0 and value < len(dList) and value != index:
        partner = dList[value]
        if partner == index:
            print("Pair: %s:%s" % (index, value))
            sum += index + value
            dList[value] = 0
            dList[index] = 0
print(sum)