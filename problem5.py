factors = [i for i in range(11,20)]
for i in range(20*19, 99999999999, 20):
    good = True
    for factor in factors:
        if i%factor != 0:
            good = False
            break
    if good:
        print(i)
        break