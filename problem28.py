#Number spiral diagonals

if __name__ == '__main__':
    sum = 1
    increment = 2
    num = 1
    while num < 1002001:
        for x in range(4):
            num = num + increment
            sum += num
        increment += 2
    print(sum)