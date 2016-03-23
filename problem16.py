# find some of digits in 2^1000

def getExponentAsList(base, exponent):
    # only works for bases up to 9
    number = [1]
    for i in range(0, exponent):
        carry = 0
        for index, digit in enumerate(number):
            digitProduct = digit * base + carry
            number[index] = digitProduct % 10
            carry = int(digitProduct / 10)
        if carry > 0:
            number.append(carry)
    number.reverse()
    return number
        
number = getExponentAsList(2, 1000)
print(number)
sumOfNumber = 0
for digit in number: sumOfNumber += digit

print(sumOfNumber)