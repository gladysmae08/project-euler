# pythagorean theorem

def pythagorean(n):
    for a in range(1, int(n/3)):
        b = n*(a - n/2) / (a - n)
        if b - int(b) != 0:
            continue
        c = 1000 - a - b
        if c*c == a*a + b*b:
            return a*b*c
            
print(pythagorean(1000))