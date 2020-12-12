file = open("Day1_input.txt",'r')
numbers = [int(n) for n in file.read().split('\n')]

#print(numbers)

for number1 in numbers:
	for number2 in numbers:
		for number3 in numbers:
			if number1 + number2 + number3 == 2020:
				print(number1 * number2 * number3)