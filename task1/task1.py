import re

numbers = []
words = []
print("Enter your string: ", end="")
userInput = input().split()
for elem in userInput:
	numbers.extend(re.findall('(\d+)', elem))
for elem in userInput:
	words.append("".join(re.findall('(\D+)', elem)))
for i in range(len(numbers)):
	numbers[i] = int(numbers[i])
for i in range(len(numbers)):
	if numbers[i] != max(numbers):
		print(pow(numbers[i], i), end = " ")
print()
print(numbers)
for i in range(len(words)):
	words[i] = words[i].title()[0:-1]+words[i][-1].upper()
print(" ".join(words))
