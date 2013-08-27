def average(scores_in):
	return sum(scores_in)/len(scores_in)

def printgrades():
	print(lines[i][0],'{0:.2f}'.format(average(grades)))

def printtotal(a):
	num_students = a[0][0]
	total=0
	del a[0]
	for i,x in enumerate(a):
		[*grades] = list(map(int,a[i][1:]))
		records.append(grades)
		total = total + sum(grades)/len(grades)
		
	print('{0:.2f}'.format(total/float(num_students)))


records = []
with open('PythonClass/grades.txt') as f:
	lines = [tuple(line.split()) for line in f]
	printtotal(lines)

	for i,x in enumerate(lines):
		[*grades] = list(map(int,lines[i][1:]))
		printgrades()