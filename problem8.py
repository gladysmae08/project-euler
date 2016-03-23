# largest contiguous product

def getProduct(input_block, start, stop):
    product = 1
    for i in input_block[start:stop+1]:
        product *= int(i)
    return product

def largestProduct(input_block, sivLength):
    start = 0
    end = sivLength-1
    product = getProduct(input_block, start, end)
    max_product = product
    while end < len(input_block)-1:
        if input_block[end+1] == '0':
            start = end+1
            end += sivLength
            continue 
        if input_block[start] != '0':
            product = product / int(input_block[start]) * int(input_block[end+1])
        else:
            product = getProduct(input_block, start+1, end+1)
        start += 1
        end += 1
        if product > max_product:
            max_product = product
    return max_product

with open("problem8_input.txt") as f:
    file_input = ''.join([line.strip() for line in f.readlines()])
print(largestProduct(file_input, 13))
