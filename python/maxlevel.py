class animal:
	num = 71 # Maximum number of animals currently appearing
	exp = 21 # Total experience value obtained from animals

animal = animal()
exp = animal.num * animal.exp

level = 0
while exp > 0:
	level = level + 1
	if level >= 1 and level <= 10:
		exp = exp - 5
	elif level >= 11 and level <= 35:
		exp = exp - 10
	elif level == 36:
		exp = exp - 12
	elif level == 37:
		exp = exp - 13
	elif level >= 38 and level <= 39:
		exp = exp - 14
	elif level >= 40 and level <= 41:
		exp = exp - 16
	elif level == 42:
		exp = exp - 18
	elif level >= 43:
		exp = exp - 20

print level
