# convert numbers to words, count characters

one_column = [ '', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine' ]
tens_column = [ '', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety' ]
exceptions = {
              10 : 'ten',
              11 : 'eleven',
              12 : 'twelve',
              13 : 'thirteen',
              14 : 'fourteen',
              15 : 'fifteen',
              16 : 'sixteen',
              17 : 'seventeen',
              18 : 'eighteen',
              19 : 'nineteen'
              }

def numberToWord(number):
    # works for numbers up to 9999
    words = ''
    tens = 0
    if number >= 1000:
        thousands = int(number / 1000)
        words += one_column[thousands] + ' ' + 'thousand'
    if number >= 100:
        hundreds = int((number % 1000) / 100)
        if hundreds != 0:
            words += ' ' + one_column[hundreds]+ ' hundred'
    if number >= 10:
        tens = int((number % 100) / 10)
        if tens != 0:
            if number >= 100:
                words += ' and '
            if tens == 1:
                words += exceptions[number % 100]
                return words
            else:
                words += tens_column[tens]
    if number > 0:
        ones = number % 10
        if ones != 0:
            if tens == 0 and number >= 100:
                words += ' and'
            words += ' ' + one_column[ones]
    return words.strip()

# sum characters in words for numbers 1-1000
charSum = 0
for i in range(1,1001):
    words = numberToWord(i)
    words = words.replace(' ', '')
    charSum += len(words)
    print(words)
print(charSum)
    
        