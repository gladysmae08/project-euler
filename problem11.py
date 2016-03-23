def getProduct(input_block, start, stop):
    product = 1
    for i in input_block[start:stop]:
        product *= int(i)
    return product

def rowProduct(matrix, length):
    maxProduct = 0
    for row in matrix:
        start = 0
        while start + length <= len(row):
            product = getProduct(row, start, start+length)
            if product > maxProduct:
                maxProduct = product
            start += 1
    return maxProduct
            
def columnProduct(matrix, length):
    flippedMatrix = list(zip(*matrix))
    return rowProduct(flippedMatrix, length)

def diagonalProduct(matrix,length):
    maxProduct = 0
    for rowIndex,row in enumerate(matrix[:-3]):
        for colIndex,col in enumerate(row[:-3]):
            product = int(matrix[rowIndex][colIndex]) * int(matrix[rowIndex+1][colIndex+1]) * int(matrix[rowIndex+2][colIndex+2]) * int(matrix[rowIndex+3][colIndex+3])
            if product > maxProduct:
                maxProduct = product
    return maxProduct

def revDiagonalProduct(matrix, length):
    flippedMatrix = []
    for line in matrix:
        flippedMatrix.append(line[::-1])
    return diagonalProduct(flippedMatrix, length)

with open('problem11_input.txt') as f:
    matrix = []
    for line in f.readlines():
        matrix.append(line.strip().split())

length = 4
answer = max(rowProduct(matrix, length), columnProduct(matrix, length), diagonalProduct(matrix, length), revDiagonalProduct(matrix, length))
print(answer)