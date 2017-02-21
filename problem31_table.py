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
                table[i][j] = 1
            else:
                # Case 1: If coin value is greater than column value, 
                #         take total from previous row's cell.
                if coins[i] > values[j]:
                    table[i][j] = table[i-1][j]
                # Case 2: Else, sum totals from previous denom's cell (above),
                #         and the total from current denom row, in the current
                #         [value - denom] column (left).
                else:
                    table[i][j] = table[i-1][j] + table[i][j - coins[i]]

    print("Time: %s" % (default_timer() - start))
    print("Ways to make change:", table[-1][-1])
