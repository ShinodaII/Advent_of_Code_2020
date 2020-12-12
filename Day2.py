import re

file = open("Day2_input.txt",'r')
lines = file.read().split('\n')
#print(lines)
c = 0
for line in lines:
	pattern = re.compile(r'(\d+)-(\d+)\s(.):\s(.*)')
	print(pattern)
	m = pattern.search(line)
	print(m)
	low, high, char, string = int(m.group(1)), int(m.group(2)), m.group(3), list(m.group(4))
	if (string[low - 1] == char) ^ (string[high - 1] == char):
		c += 1
print(c)
