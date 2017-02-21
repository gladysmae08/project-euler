from timeit import default_timer

# Initialize Dynamic Programming table to all zeroes
coins = [1, 2, 5, 10, 20, 50, 100, 200]
values = [ x+1 for x in range(0,200) ]
table = [[0 for x in range(len(values))] for x in range(len(coins))]

if __name__ == "__main__":
    start = default_timer()
    for j in range(len(values)):
        for i in range(len(coins)):
            if coins[i] == 1:
                print("i: %s, j: %s" % (i, j))
                table[i][j] = 1
            else:
                # Case 1: coin value greater than column value, 
                #         take value from left cell
                if coins[i] > values[j]:
                    table[i][j] = table[i-1][j]
                # Case 2: (Not necessary, small optimization) If coin value
                #         equals column value, total is prev denom total + 1
                elif coins[i] == values[j]:
                    table[i][j] = table[i][j-1] + 1
                # Case 3: take values from previous denom's cell, and the value
                #         from current denom row, in the current value - denom
                #         value column
                else:
                    table[i][j] = table[i-1][j] + table[i][j - coins[i]]
    print("Time: %s" % (default_timer() - start))
    print("Ways to make change:", table[-1][-1])