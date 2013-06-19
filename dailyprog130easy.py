import random
import sys

die = sys.argv[1]

attr = die.split('d')

rolls = attr[0]
sides = attr[1]

output = []

for x in range(int(rolls)):
	output.append(random.randint(2,int(sides)))

print output