import re

file = open("Day4_input.txt",'r')
passports = re.split("\n\n", file.read())
c = 0
#print(passports[:10])
fields = ('byr','iyr','eyr','hgt','hcl','ecl','pid')
values = []
items = []
for passport in passports:
	if all(field in passport for field in fields):
		for field in fields:
			values.append(re.search(field + r':(\S+)', passport).groups(1)[0])
		items.append({field: value for field, value in zip(fields, values)})
	values = []

results = []
for item in items:
	#print(item)
	results.append(len(item['byr']) == 4 and 1920 <= int(item['byr']) <= 2002)

	results.append(len(item['iyr']) == 4 and 2010 <= int(item['iyr']) <= 2020)

	results.append(len(item['eyr']) == 4 and 2020 <= int(item['eyr']) <= 2030)

	if item['hgt'].endswith('cm'):
		results.append(150 <= int(item['hgt'][:-2]) <= 193)
	elif item['hgt'].endswith('in'):
		results.append(59 <= int(item['hgt'][:-2]) <= 76)
	else:
		results.append(False)

	if len(item['hcl']) == 7 and item['hcl'].startswith('#'):
		try:
			#print(item['hcl'])
			int(item['hcl'][1:],16)
		except ValueError:
			results.append(False)
		else:
			results.append(True)
	else:
		results.append(False)
	results.append(item['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'])

	results.append(len(item['pid']) == 9 and all(digit.isdigit() for digit in item['pid']))

	if all(results):
		c += 1
		#print(item)

	results = []

print(c)