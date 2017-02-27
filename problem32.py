from itertools import permutations
from timeit import default_timer

ints = [ str(x) for x in range(1,10) ]

if __name__ == '__main__':
    products = []
    start = default_timer()
    for perm in permutations(ints, 9):
        product = int(''.join(perm[-4:]))
        if product in products:
            continue
        # split remaining numbers for multiplicants
        if int(''.join(perm[:1])) * int(''.join(perm[1:5])) == product:
            products.append(product)
        elif int(''.join(perm[:2])) * int(''.join(perm[2:5])) == product:
            products.append(product)
        else:
            continue
    sum = 0
    for product in products:
        print(product)
        sum += product
    time = default_timer() - start
    print("Time: %s" % time)
    print("Sum: %s" % sum)

        

