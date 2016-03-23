def dynamicCollatz(n):
    # initialize list of length n to -1
    counts = {}
    counts[1] = 1
    maxIndex = 1
    # iterate from 2 to n populating counts list along the way
    for num in range(2,n+1):
        print("evaluating %d" % num)
        current = num
        if current in counts:
            continue
        # store new values in dictionary
        newCollatzValues = {num:1}
        while current != 1:
            current = getCollatz(current)
            if current in counts:
                for key in newCollatzValues:
                    newCollatzValues[key] += counts[current]
                break
            else:
                for key in newCollatzValues:
                    newCollatzValues[key] += 1
                newCollatzValues[current] = 1
        # add new values to counts array
        for key in newCollatzValues:
            counts[key] = newCollatzValues[key]
        if counts[num] > counts[maxIndex]:
            maxIndex = num
    # return max index/starting value
    return maxIndex

def getCollatz(n):
    ''' Helper method'''
    if n%2==0:
        return int(n/2)
    else:
        return int(n*3 + 1)

print(dynamicCollatz(1000000))
    