type = input("Newton's second law of motion, voltage, wave speed, time, or distance: ")
if type == "voltage":
	I = float(input("give the current: "), "amp")
	R = float(input("give the resistance: "))
	total = I*R
	print((total), "volts")
elif type == "time":
	d = float(input("give the distance: "))
	s = float(input("give the speed: "))
	total = d/s
	print((total), "s")
elif type == "distance":
	t = float(input("give the time: "))
	s = float(input("give the speed: "))
	total = t*s
	print((total), "m")
elif type == "wave speed":
	f = float(input("give the frequency: "))
	λ = float(input("give the wavelength: "))
	total = f*λ
	print((total), "v")
elif type == "newton's second law of motion":
	m = float(input("Force (F) = Mass (m) × Acceleration (a). Give the mass: "))
	a = float(input("give the acceleration: "))
	total = m*a
	print((total), "N")