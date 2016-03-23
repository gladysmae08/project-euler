# largest palindrome of product of two 3-digit numbers
from test.test__locale import candidate_locales
max = 999

def palindrome(candidate):
    candidate = str(candidate)
    first = 0
    last = len(candidate)-1
    while last > first:
        if candidate[first]!=candidate[last]:
            return False
        first += 1
        last -= 1
    return True
        
for i in range(999, 100, -1):
    for j in range(i, 100, -1):
        product = i * j
        if(product > max and palindrome(product)) :
            max = product
print(max)