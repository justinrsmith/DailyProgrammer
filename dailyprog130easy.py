import random
import sys

die = sys.argv[1]

attr = die.split('d')
rolls, sides = sys.argv[1].split('d')

result = []

result = ' '.join([str(random.randrange(1, int(sides)+1)) for die in range(int(rolls))])

print result