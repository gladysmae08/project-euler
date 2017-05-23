from math import factorial
from timeit import default_timer

factorials = { 
               '0' : factorial(0),
               '1' : factorial(1),
               '2' : factorial(2),
               '3' : factorial(3),
               '4' : factorial(4),
               '5' : factorial(5),
               '6' : factorial(6),
               '7' : factorial(7),
               '8' : factorial(8),
               '9' : factorial(9)
              }

def isCurious(num):
    digits = str(num)
    sum = 0
    for digit in digits:
        sum += factorials[digit]
    return num == sum

if __name__ == "__main__":
        start = default_timer()
        curious = []
        # upperbound is 9! * 7 = 2540160 since that is the largest dusty
        for number in range(100,2540160):
            if isCurious(number):
                curious.append(number)
        total_time = default_timer() - start
        for c in curious: print(c)
        print("sum: ", sum(curious))
        print("time: ", total_time)

            