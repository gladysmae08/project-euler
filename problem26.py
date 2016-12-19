import re
import decimal
decimal.getcontext().prec = 10000

def re_back_ref(decimal_str):
    '''Use regex to find repeating sequence in string'''
    pattern = '0\\..*?([0-9]{3,}?)\\1{1,}.*'
    prog = re.compile(pattern)
    result = prog.match(decimal_str)

    if result:
        return result.group(1)
    return ''


max = 0
d = -1
longest_result = ''
for i in range(2,1001):
    result = re_back_ref(str(decimal.Decimal(1) / decimal.Decimal(i)))
    if len(result) >= max:
        max = len(result)
        d = i
        longest_result = result

print("d = %s" % d)
print("length = %s" % max)


