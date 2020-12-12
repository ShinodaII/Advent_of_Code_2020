from functools import reduce
file = open("Day6_input.txt")
groups = file.read().split("\n\n")
count = 0
for group in groups:
	count += len(reduce(lambda set1,set2: set1.intersection(set2), map(set, group.split('\n'))))

	#print(' '.join(group.split('\n')) + ": " + str(count))
print(count)