'''
Problem 22:  Convert names to ascii scores
COLIN = 3 + 15 + 12 + 9 + 14 = 53
'''

def asciiToInt(word):
	sum = 0
	word = word.upper()
	for char in word:
		sum += ord(char) - 64
	return sum

with open('problem22_input.txt') as fp:
	text = fp.read()
	input_words = [ word.strip('"') for word in text.split(',') ]
	input_words.sort()

total = 0
for index, word in enumerate(input_words):
	total += (index + 1) * asciiToInt(word)
print(total)
