import sys

s = list(sys.argv[1])
results = []
results.append(sys.argv[1])

while len(s)>1:
	total = str(sum(int(b) for b in s))
	results.append(total)
	s = list(total)

print results