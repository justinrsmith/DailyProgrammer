def calc_max_leds(timespan, capacity, current):
	serial_max_leds = 5
	max_leds = int((capacity / (current * timespan)) * serial_max_leds)

	return max_leds

def calc_resistance(voltage, timespan):
	needed_voltage = voltage - 1.2
	resistance = (needed_voltage/1.2) * timespan
	print 'Resistor: %s Ohms' % float("{0:.2f}".format(resistance))

def draw_circuit(max_leds):
	serials = max_leds / 5 # a serial can have a max of 5 LEDs
	led = '-|>|-'
	output = ''
	serial_connect = ' |                             |\n'

	for x in range(serials):
		line = '-'
		for y in range(5):
			line = line + led + '-'
		if x == 0:
			line = '*' + line + '*'
		else:
			line = ' ' + line 

		output = output + line + '\n'
		if (x!=(serials-1)):
			output = output + serial_connect

	print output

while True:
	try:
		print('Please provide LED voltage, current, battery voltage, capacity, and timespan.')
		user_input = raw_input('> ').split()
		user_input = [float(i) for i in user_input]
		voltage, current, voltave, capacity, timespan = user_input
		calc_resistance(voltage, timespan)
		max_leds = calc_max_leds(timespan, capacity, current)
		draw_circuit(max_leds)
	except ValueError:
		print('Please enter only numbers and make sure to provide all values.')
