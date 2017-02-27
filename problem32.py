from itertools import permutations

ints = [ str(x) for x in range(1,10) ]

if __name__ == '__main__':
    products = []
    for perm in permutations(ints, 9):
        product = int(''.join(perm[-4:]))
        if product in products:
            continue
        # split remaining numbers for multiplicants
        if int(''.join(perm[:1])) * int(''.join(perm[1:5])) == product:
            products.append(product)
        elif int(''.join(perm[:2])) * int(''.join(perm[2:5])) == product:
            products.append(product)
        elif int(''.join(perm[:3])) * int(''.join(perm[3:5])) == product:
            products.append(product)
        elif int(''.join(perm[:4])) * int(''.join(perm[4:5])) == product:
            products.append(product)
        else:
            continue
    sum = 0
    for product in products:
        print(product)
        sum += product
    print("Sum: %s" % sum)

        

