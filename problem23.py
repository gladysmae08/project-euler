'''
problem 23: abundant numbers
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


abundant_numbers = []
abundant_sums = []
for integer in range(12, 21823):
	sum = sumOfFactors(integer)
	if sum > integer:
		abundant_numbers.append(integer)
		for number in abundant_numbers:
			abundant_sums.append(integer + number)


all_nums = range(1, 21824)
non_sums = list(set(all_nums) - set(abundant_sums))
total = 0
for num in non_sums:
	total += num
print(total)