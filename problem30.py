#Digit fifth powers

power_array = [ x**5 for x in range (0, 10) ]

def get_fifth_power_sum(value):
    sum = 0
    for x in str(value):
        sum += power_array[int(x)]
    return int(sum)

def get_fifth_power_sum2(value):
    sum = 0
    while value > 0:
        x = value % 10
        sum += power_array[x]
        value = int(value / 10)
    return int(sum)

if __name__ == "__main__":
    import timeit
    results = []
    x = 1000
    start_time = timeit.default_timer()
    while(x < 354295):
        sum = get_fifth_power_sum(x)
        if sum == x:
            results.append(x)
            x += 1
        elif sum > x:
            x = (int)((int(x / 10) + 1) * 10)
        else:
            x += 1
    elapsed = timeit.default_timer() - start_time
    print("gen time: %s" % elapsed)
    sum = 0
    for x in results:
        sum += x
    print(results)
    print(sum)