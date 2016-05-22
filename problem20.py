# 100!

'''
[2][4]
x  [5]
-------
[1][2][0]

     [2][4]
x    [1][2]
----------
    [4][8]
 [2][4][0]
----------
 [2][8][8]
 
 
  999
  x99
-----
 8991
89910
-----
98901
'''


def multiply_lists(L1, L2):
    result = []
    for index, i in enumerate(L2[::-1]):
        row_result = []
        if index > 0:
            row_result.append(0)
        carry_over = 0
        for j in L1[::-1]:
            product = i * j + carry_over
            if product > 9:
                ones_column = product % 10
                carry_over = int(product / 10)
                row_result.append(ones_column)
            else:
                row_result.append(product)
                carry_over = 0
        if carry_over > 0:
            row_result.append(carry_over) 
        result = add_lists(row_result[::-1], result)
    return result
                                  
def add_lists(L1, L2):
    result = L1[::-1]
    for index, value in enumerate(L2[::-1]):
        if len(result) > index:
            sum = result[index] + value
            result[index] = sum % 10
            tempIndex = index + 1
            while(sum >= 10):
                if len(result) == tempIndex:
                    result.append(1)
                    break
                else:
                    sum = result[tempIndex] + 1
                    result[tempIndex] = sum % 10
                    tempIndex += 1
    return result[::-1]                     
                
def list_factorial(base):
    result = [1]
    for i in range(1, base+1):
        # create list from int
        int_list = [ int(x) for x in str(i)]
        result = multiply_lists(result, int_list)
    return result

factorial = list_factorial(100)
print(factorial)
print(len(factorial))
sum = 0
for i in factorial:
    sum += i
print(sum)