from functools import reduce

file = open("Day3_input.txt",'r')
lines = file.read().split('\n')

l = len(lines[0])
c_list = []

p1, p2, p3, p4 = 0, 0, 0, 0
c1, c2, c3, c4 = 0, 0, 0, 0
for line in lines:
	if line[p1 % l] == '#':
		c1 += 1
	if line[p2 % l] == '#':
		c2 += 1
	if line[p3 % l] == '#':
		c3 += 1
	if line[p4 % l] == '#':
		c4 += 1
	
	p1 += 1
	p2 += 3
	p3 += 5
	p4 += 7
	#print(c)
c_list.extend([c1, c2, c3, c4])

p5, c5 = 0, 0
for line in lines[::2]:
	if line[p5 % l] == '#':
		c5 += 1
	p5 += 1

c_list.append(c5)

ans = reduce(lambda x, y : x * y, c_list)
print(ans)

